import pybullet as p
import pybullet_data
import time

# Connect to PyBullet with a visible window
p.connect(p.GUI)

# Set up the environment
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Load a ground plane
p.loadURDF("plane.urdf")

# Load a robot arm (Kuka is a real industrial robot arm)
robot = p.loadURDF("kuka_iiwa/model.urdf", basePosition=[0, 0, 0])

# Keep the simulation running
print("Robot arm loaded. Close the window to exit.")
while True:
    p.stepSimulation()
    time.sleep(1./240.)