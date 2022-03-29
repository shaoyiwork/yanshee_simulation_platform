# yanshee_simulation_platform


#  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Yanshee 仿真平台 
#### &emsp;&emsp;是一套基于Webots仿真环境开发的用来模拟Yanshee机器人各种功能的教学与竞赛场景设计平台。主要功能包括：
####  运动控制、传感器系统、灯效设置、视觉识别等四大部分。面向用户提供两种二次开发接口：用户ROS接口、YanAPI接口。
#### 详情请参考《Yanshee仿真平台使用手册V1.0》。
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
#### 步骤1、拷贝或克隆所有工程文件到Ubuntu18.04环境下。例如：/home/用户目录下。
#### 步骤2、使用命令安装yanshee-ros服务deb文件包
#### &emsp;&emsp;&emsp;sudo dpkg -i UBT-YansheeSimulation-Ros-Linux-v1.0.3-xxx.deb
#### 步骤3、安装依赖包。命令行：cd deps 然后 ./install.sh 等待安装完成。 
#### 步骤4、添加yanshee-ros服务到环境变量中，编辑 ~/.bashrc 文件最后一行添加
#### &emsp;&emsp;&emsp; source /opt/yanshee/setup.bash
#### &emsp;&emsp;&emsp; 保存退出。然后使用命令source .bashrc使其生效。
#### 步骤5、 另起窗口，输入roscore，启动ros主程序。
#### 步骤6、 另起窗口，输入如下命令，启动yanshee-ros服务。
#### &emsp;&emsp;&emsp; roslaunch yanshee_launch yanshee.launch
#### 步骤7、 另起窗口，命令行webots之后，打开yanshee_simulation_project/worlds目录下相应的wbt场景文件，点击运行按钮，即可开始仿真。
