import asyncio
import json
import random
from typing import Literal, Any

CallOutcome = Literal['success', 'failure']

async def send_call(job_id: str, metadata: Any) -> CallOutcome:
    """
    Simulates making a call with a job ID and metadata.
    
    Args:
        job_id: The ID of the job
        metadata: Additional metadata for the call
        
    Returns:
        CallOutcome: Either 'success' or 'failure'
    """
    print(f"Sending call for jobId: {job_id} with metadata: {json.dumps(metadata)}")
    
    # Simulate call duration (2-5 seconds)
    duration = random.uniform(2.0, 5.0)
    await asyncio.sleep(duration)
    
    # Random success/failure (70% success rate)
    success = random.random() < 0.7
    
    print(f"Call for jobId: {job_id} with metadata: {json.dumps(metadata)} "
          f"completed with outcome: {'success' if success else 'failure'}")
    
    return 'success' if success else 'failure' 