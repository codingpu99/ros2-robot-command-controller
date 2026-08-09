import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class CommandController(Node):

    def __init__(self):
        super().__init__('command_controller')

        self.subscription = self.create_subscription(
            String,
            'robot_command',
            self.command_callback,
            10
        )

    def command_callback(self, msg):
        command = msg.data

        if command == 'FORWARD':
            self.get_logger().info('Robot moving forward')
        elif command == 'LEFT':
            self.get_logger().info('Robot turning left')
        elif command == 'RIGHT':
            self.get_logger().info('Robot turning right')
        elif command == 'STOP':
            self.get_logger().info('Robot stopped')


def main(args=None):
    rclpy.init(args=args)

    node = CommandController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()