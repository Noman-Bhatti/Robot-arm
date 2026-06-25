import pybullet as p
import pybullet_data
import time
import math

# Connect to PyBullet with a visible window
p.connect(p.GUI)

# Set up the environment
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Load a ground plane
p.loadURDF("plane.urdf")

# Load a robot arm (Kuka is a real industrial robot arm)
robot = p.loadURDF("kuka_iiwa/model.urdf", basePosition=[0, 0, 0])

# Find out how many joints this arm has
num_joints = p.getNumJoints(robot)
print(f"This robot arm has {num_joints} joints")

# Print info about each joint so we understand the arm's structure
for i in range(num_joints):
    joint_info = p.getJointInfo(robot, i)
    joint_name = joint_info[1].decode("utf-8")
    print(f"Joint {i}: {joint_name}")

print("Robot arm loaded. Watch joint 3 move. Close the window to exit.")

# Keep the simulation running and move one joint back and forth
t = 0
while True:
    # Calculate a smooth back-and-forth angle using sine wave
    target_angle = math.sin(t) * 1.0  # swings between -1 and 1 radian

    # Move joint index 3 to the target angle
    p.setJointMotorControl2(
        bodyIndex=robot,
        jointIndex=3,
        controlMode=p.POSITION_CONTROL,
        targetPosition=target_angle
    )

    p.stepSimulation()
    time.sleep(1. / 240.)
    t += 1. / 240.