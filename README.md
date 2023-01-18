#### &emsp;&emsp;&emsp;&emsp;&emsp;

## Yanshee 仿真平台
#### 是一套基于Webots仿真环境开发的用来模拟Yanshee机器人各种功能的教学与竞赛场景设计平台。
#### 涉及机器人运动控制、传感器系统、灯效设置、视觉识别等四大部分。
#### 并且面向用户提供两种二次开发接口：通用ROS1接口、YanAPI接口。
#### 详情请参考《Yanshee仿真平台使用手册V1.0》。
#### &emsp;&emsp;&emsp;&emsp;&emsp;

### 主要功能详细说明：
#### 1、提供完整的Yanshee机器人Webots仿真模型（包括17个舵机组件、摄像头、传感器、胸前灯和身体结构组件等）
#### 2、集成各功能模块ROS使用服务和话题。
#### 3、集成Restful风格的http服务模块。
#### 4、提供控制机器人基本功能的用户ROS使用Demo案例。
#### 5、提供控制机器人基本功能的用户YanAPI接口使用Demo案例。
#### 6、运动控制功能包括：步态控制、motion文件执行和舵机控制。
#### 7、传感器包括：左右红外传感器和IMU运动传感器使能与读取。
#### 8、灯效设置包括：眼睛灯和胸前灯颜色和模式设置。
#### 9、视觉人脸功能包括：人脸检测、人脸录入、人脸识别、年龄、性别、眼镜、口罩、表情识别等。
#### 10、视觉其他功能包括：拍照、手势识别、物体识别、颜色识别、Apriltag二维码识别、QR二维码识别等。
#### 11、提供一站式Yanshee仿真平台从部署安装到使用设计的整体解决方案。
#### &emsp;&emsp;&emsp;&emsp;&emsp;
### 工程包文件内容说明：
#### UBT-YansheeSimulation-Ros-Linux-v1.0.3_20220329_Release_CN.deb ——	用来安装Yanshee虚拟仿真机器人ROS服务的压缩包文件
#### deps ——	安装yanshee仿真环境的ros服务所需要的依赖包
#### user_demo/ros_demo —— 用户控制机器人所有功能的ROS接口使用demo
#### user_demo/YanAPI_demo —— 用户控制机器人所有功能的YanAPI接口使用demo
#### yanshee_simulation_project/worlds —— webots软件环境所需的wbt文件
#### yanshee_simulation_project/model —— Yanshee机器人的wbo模型文件
#### yanshee_simulation_project/controllers —— Yanshee的控制器执行文件
#### yanshee_simulation_project/scripts —— 用于将hts转成motion文件的脚本
#### yanshee_simulation_project/motion —— 存放motion动作文件的位置

#### &emsp;&emsp;&emsp;&emsp;&emsp;
### 如何使用仿真平台：
#### 1、拷贝或克隆所有工程文件到Ubuntu18.04环境下。例如：/home/用户目录下。
#### 2、使用命令安装yanshee-ros服务deb文件包
#### &emsp;&emsp;&emsp;sudo dpkg -i UBT-YansheeSimulation-Ros-Linux-v1.0.3-xxx.deb
#### 3、安装依赖包。命令行：cd deps 然后 ./install.sh 等待安装完成。 
#### 4、添加yanshee-ros服务到环境变量中，编辑 ~/.bashrc 文件最后一行添加
#### &emsp;&emsp;&emsp; source /opt/yanshee/setup.bash
#### &emsp;&emsp;&emsp; 保存退出。然后使用命令source .bashrc使其生效。
#### 5、 另起窗口，输入roscore，启动ros主程序。
#### 6、 另起窗口，输入如下命令，启动yanshee-ros服务。
#### &emsp;&emsp;&emsp; roslaunch yanshee_launch yanshee.launch
#### 7、 另起窗口，命令行webots之后，打开yanshee_simulation_project/worlds目录下相应的wbt场景文件，点击运行按钮，即可开始仿真。
#### 8、运行示例demo，另起窗口，cd user_demo/YanAPI_demo/ 例如让机器人做动作：python3 motion_test.py 查看仿真机器人效果变化。

#### &emsp;&emsp;&emsp;&emsp;&emsp;
#### &emsp;&emsp;&emsp;&emsp;&emsp;
