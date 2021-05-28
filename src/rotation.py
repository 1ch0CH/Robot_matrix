import numpy as np
import math

def rotation(vx,vy,vz, VX, VY, VZ):
  # v is A coordinates
  # V is B coordinates
  # B -> A A에서 바라본 B
  
  r11 = np.inner(VX,vx)
  r21 = np.inner(VX,vy)
  r31 = np.inner(VX,vz)
  r12 = np.inner(VY,vx)
  r22 = np.inner(VY,vy)
  r32 = np.inner(VY,vz)
  r13 = np.inner(VZ,vx)
  r23 = np.inner(VZ,vy)
  r33 = np.inner(VZ,vz)

  R = np.array([[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]])
  return R

# (y,x) atan(y/x)
def matrix_to_rpy(R):
  A = math.atan2(R[1][0], R[0][0])
  B = math.atan2(-R[2][0], math.sqrt((R[2][1]) ^ 2 + (R[2][2]) ^ 2))
  C = math.atan2(R[2][1], R[2][2])

  return A, B, C # alpha , beta, gamma
  
  
vx = np.array([0,-1,0])
vy = np.array([1,0,0])
vz = np.array([0,0,1])
VX = np.array([1, 0, 0])
VY = np.array([0, 1, 0])
VZ = np.array([0, 0, 1])
R = rotation(vx,vz,vy,VX,VY,VZ)

A,B,C=matrix_to_rpy(R)
a = A/math.pi*180
print(a)
