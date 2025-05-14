import asyncio
from websockets import * 

async def sendData(websocket, key, value):    
    await websocket.send(f"{key},{value}")


async def ArmGo(websocket):
    print("aadd")

    for i in range(90, 181):
        await sendData(websocket, "Shoulder", i)
        await asyncio.sleep(0.01)
    for i in range(90, 60, -1):
        await sendData(websocket, "Elbow", i)
        await asyncio.sleep(0.01)
    for i in range(90, -1, -1):
        await sendData(websocket, "Gripper", i)
        await asyncio.sleep(0.01)

    # await asyncio.sleep(0.1)
    
    for i in range(60, 91):
        await sendData(websocket, "Elbow", i)
        await asyncio.sleep(0.01)
    for i in range(180, 89, -1):
        await sendData(websocket, "Shoulder", i)
        await asyncio.sleep(0.01)
    for i in range(90, -1, -1):
        await sendData(websocket, "Base", i)
        await asyncio.sleep(0.01)
        
    # await asyncio.sleep(0.1)
    

    for i in range(90, 150):
        await sendData(websocket, "Shoulder", i)
        await asyncio.sleep(0.01)
    for i in range(90, 60, -1):
        await sendData(websocket, "Elbow", i)
        await asyncio.sleep(0.01)
    for i in range(0, 170):
        await sendData(websocket, "Gripper", i)
        await asyncio.sleep(0.01)
        
    # await asyncio.sleep(0.1)
    

    for i in range(150, 89, -1):
        await sendData(websocket, "Shoulder", i)
        await asyncio.sleep(0.01)
    for i in range(61, 91):
        await sendData(websocket, "Elbow", i)
        await asyncio.sleep(0.01)
    for i in range(170, 89, -1):
        await sendData(websocket, "Gripper", i)
        await asyncio.sleep(0.01)
        
    for i in range(0, 91):
        await sendData(websocket, "Base", i)
        await asyncio.sleep(0.01)
        
    await sendData(websocket, "automation_done", "ON")
