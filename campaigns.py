from abc import ABC, abstractmethod
import time
import uuid
from datetime import datetime, timedelta
from src.utils import send_call
import asyncio

class Campaign:
    def __init__(self, name, start_time, retry_attempts, interval):
        self.name = name
        self.start_time = start_time
        self.retry_attempts = retry_attempts
        self.interval = interval

class JobStatus:
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class Job(ABC):
    def __init__(self, status):
        self.job_id = str(uuid.uuid4())
        self.status = status
        self.last_attempt_time = None
        self.current_attempt = 0

    @abstractmethod
    def is_ready(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class CallJob(Job):
    def __init__(self, campaign):
        super().__init__(JobStatus.PENDING)
        self.campaign = campaign

    def is_ready(self):
        # Check if the last attempt was more than the interval ago
        if self.last_attempt_time is None:
            return True # update this to use start time later
        
        return datetime.now() - self.last_attempt_time > timedelta(seconds=self.campaign.interval)

    async def execute(self):

        # Send the call
        self.current_attempt += 1
        result = await send_call(self.job_id, {"campaign_name": self.campaign.name, "attempt": self.current_attempt, "time_attempted": datetime.now().isoformat()})
        self.last_attempt_time = datetime.now()

        if result == 'success':
            self.status = JobStatus.COMPLETED
            print(f"Called {self.campaign.name} successfully")
            return "success"

        if self.current_attempt >= self.campaign.retry_attempts:
            self.status = JobStatus.FAILED
            print(f"Failed to call {self.campaign.name} after {self.campaign.retry_attempts} attempts")
            return "failed"

        return "retry"

class JobManager:
    def __init__(self):
        self.jobs = []

    def add_job(self, job):
        self.jobs.append(job)

    async def execute_all_jobs(self):
        
        while len(self.jobs) > 0:
            job = self.jobs.pop(0)
            if job.is_ready():
                result = await job.execute()
                if result == "retry":
                    self.add_job(job)
            else:
                # If job is not ready, add it back to the queue
                self.add_job(job)

if __name__ == "__main__":
    campaign = Campaign("Test Campaign", datetime.now(), 3, 4)
    job = CallJob(campaign)
    job_manager = JobManager()
    job_manager.add_job(job)
    asyncio.run(job_manager.execute_all_jobs())

        

