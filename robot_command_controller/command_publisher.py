import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class CommandPublisher(Node):

    def __init__(self):
        super().__init__('command_publisher')

        self.publisher = self.create_publisher(
            String,
            'robot_command',
            10
        )

        self.timer = self.create_timer(2.0, self.publish_command)

        self.commands = ['FORWARD', 'LEFT', 'RIGHT', 'STOP']
        self.index = 0

    def publish_command(self):
        msg = String()
        msg.data = self.commands[self.index]

        self.publisher.publish(msg)
        self.get_logger().info(f'Command: {msg.data}')

        self.index = (self.index + 1) % len(self.commands)


def main(args=None):
    rclpy.init(args=args)

    node = CommandPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()