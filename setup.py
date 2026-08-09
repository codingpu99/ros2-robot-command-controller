from setuptools import find_packages, setup

package_name = 'robot_command_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Punam Bora',
    maintainer_email='geniuspu69@gmail.com',
    description='A ROS 2 robot command controller using publisher and controller nodes',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'publisher = robot_command_controller.command_publisher:main',
        'controller = robot_command_controller.command_controller:main',
    ],
},
)
