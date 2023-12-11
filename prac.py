import asyncio
import time

def print_fruits_1():
    fruits = ['apple', 'orange', 'mango', 'guava', 'banana']
    for fruit in fruits:
        print(fruit)
        time.sleep(2)

async def print_fruits(idx):
    fruits = ['apple', 'orange', 'mango', 'guava', 'banana']
    print(fruits[idx])
    await asyncio.sleep(2)

async def generate_concurrently():
    tasks = [print_fruits(idx) for idx in range(5)]
    await asyncio.gather(*tasks)

s = time.perf_counter()
asyncio.run(generate_concurrently())
elapsed = time.perf_counter() - s
print(f"Concurrent execution elapsed: {elapsed:0.2f}\n")

s = time.perf_counter()
print_fruits_1()
elapsed = time.perf_counter() - s
print(f"Serial Execution elapsed: {elapsed:0.2f}")