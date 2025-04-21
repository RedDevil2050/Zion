
import asyncio
from importlib import import_module
from backend.utils.cache_utils import disk_cache

async def run_agent_async(agent_path: str, symbol: str):
    module_path = agent_path.replace("/", ".")
    agent_module = import_module(f"backend.agents.{module_path}")
    cached = disk_cache(symbol, agent_path)
    if cached:
        return cached
    result = agent_module.run(symbol)
    disk_cache(symbol, agent_path, result)
    return result

async def run_all_agents(symbol: str, agent_paths: list):
    tasks = [run_agent_async(path, symbol) for path in agent_paths]
    return await asyncio.gather(*tasks)
