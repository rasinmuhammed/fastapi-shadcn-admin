"""
Vercel serverless handler
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from demo.app import app
from mangum import Mangum

# Mangum wraps FastAPI for AWS Lambda/Vercel compatibility  
handler = Mangum(app, lifespan="off")
