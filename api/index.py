from demo.app import app

# Vercel needs a module-level variable
# This exports the FastAPI app for Vercel's Python runtime
handler = app
