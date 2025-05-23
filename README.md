# AQ-Toolkit
> 为Blender定制的个人mod工具箱，为其他游戏mod定制的功能为可选开关  
## Blender版本3.x-4.3

### 功能
- **根据UV岛边缘分离网格** 优化法向问题
- **限制并规格化权重** 可自定义权重限值，并规格化所有权重
- **清理孤立边与顶点** 防止某些游戏由于孤立顶点导致的网格爆炸
- **保留单面** 选择活动物体并保留面索引为0的面，删除网格的其他面，可选保留面后是否开启透视模式
- **删除所选并缩放 by FT-A7** 编辑模式下，删除所选网格并在所选质心处新建三角面并缩放到最小
- **检查0权重顶点** 假设顶点上无任何顶点组权重，则选中该顶点
- **移除空顶点组** 移除模型上没有权重赋予的空顶点组
- **选择缝合边** 选择模型上所有缝合边
- **选择/移除未使用的骨骼** 根据模型带的骨骼修改器选择骨骼中没有对应网格顶点组的骨骼，可选开关是否选择后直接移除未使用骨骼
- **合并顶点组权重** 将需要合并的组改为同前缀名，（例如0，0.001，1，1.001，将分别合并为0，1两组）从0开始，往后顺延
- **骨骼吸附&顶点组重命名** 根据需要自行增添/修改字典，字典每个元素左侧为目标骨骼，右侧为原始骨骼，原始骨骼将吸附到目标骨骼的位置，支持热更新
- **导入面部法向优化模板**  可导入优化法向模板，模板自带镜像修改器和细分修改器

### 其他功能（在偏好设置中开关）
- ####  Helldivers 2
    - **删除断肢网格**  根据物体材质名称,删除所选物体所有断肢网格（可多选），必须将有断肢材质的物体设为活跃物体
- ####  Monster Hunter Wilds
    - **创建多级文件夹**  快速创建多级文件夹，建议从根目录natives\STM开始
- ####  额外工具 by FT-A7
    - **UV切割**  
    - **顶点组对比**  对比两个物体到顶点组，使两个物体相交的顶点组权重相同
    
