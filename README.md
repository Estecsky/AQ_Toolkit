# AQ-Toolkit
> 为Blender定制的个人mod工具箱，为其他游戏mod定制的功能为可选开关

## Blender版本3.x-4.0

### 功能
- **根据UV岛边缘分离网格** 优化法向问题
- **限制并规格化权重** 可自定义权重限值，并规格化所有权重
- **清理孤立边与顶点** 防止某些游戏由于孤立顶点导致的网格爆炸
- **保留单面** 选择活动物体并保留面索引为0的面，删除网格的其他面，可选保留面后是否开启透视模式
- **检查0权重顶点** 假设顶点上无任何顶点组权重，则选中该顶点
- **移除空顶点组** 移除模型上没有权重赋予的空顶点组
- **选择缝合边** 选择模型上所有缝合边
- **删除未使用的骨骼** 根据模型带的骨骼修改器移除骨骼中没有对应网格顶点组的骨骼
- **合并顶点组权重** 将需要合并的组改为同前缀名，（例如0，0.001，1，1.001，将分别合并为0，1两组）从0开始，往后顺延

### 其他功能（在偏好设置中开关）
- ####  Helldivers 2
    - **删除断肢网格**  根据物体材质名称,删除所选物体所有断肢网格（可多选），必须将有断肢材质的物体设为活跃物体
    
