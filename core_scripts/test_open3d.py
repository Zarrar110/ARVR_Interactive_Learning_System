# core_scripts/test_open3d.py
import open3d as o3d

mesh = o3d.geometry.TriangleMesh.create_sphere()
mesh.paint_uniform_color([0.2, 0.6, 0.9])
o3d.visualization.draw_geometries([mesh])
