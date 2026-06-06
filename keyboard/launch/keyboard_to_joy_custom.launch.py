import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    config_file_path = LaunchConfiguration('config_file_path')

    return LaunchDescription([
    
        DeclareLaunchArgument(
            'config_file_path',
            default_value = os.path.join(
                get_package_share_directory('keyboard'),
                'config',
                'example_config.yaml'
            )
        ),
    
        Node(
            package='keyboard',
            executable='keyboard',
            name='keyboard_node'
        ),

        Node(
            package='keyboard',
            executable='keyboard_to_joy.py',
            name='keyboard_to_joy_node',
            parameters=[{'config_file_name': config_file_path}]
        ),
    ])
