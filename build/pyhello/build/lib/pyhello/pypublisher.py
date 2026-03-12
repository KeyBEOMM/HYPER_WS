import rclpy # ROS2의 Python client library (노드 생성, publish, subscriber 기능 제공)
from rclpy.node import Node # ROS2에서 노드 생성을 위한 기본 클래스
from rclpy.qos import QoSProfile # 메시지 큐 크기, 신뢰성 설정

from std_msgs.msg import String  # C++ Subscriber와 맞추기 위해 표준 String 메시지 사용
                                    # from example_interface.msg import ExMsg # 이처럼 사용자 정의 메시지 사용가능

class PyPublisher(Node): # Node 클래스를 상속하여 PyPublisher 클래스(노드) 정의
    def __init__(self):
        super().__init__('py_publisher') # 노드 이름 설정
        qos_profile = QoSProfile(depth=10) # 메시지 큐 크기 설정 depth=10 : 발행된 메시지가 최대 10개까지 큐에 저장될 수 있도록 설정
        self.publisher_ = self.create_publisher(String, 'hello_topic', qos_profile) # String 타입의 메시지를 'hello_topic'으로 발행하는 publisher 생성
        
        timer_period = 1.0 # 1초마다 메시지 발행
        self.timer = self.create_timer(timer_period, self.timer_callback) # 타이머 생성, time period 마다 timer_callback 함수 호출

        self.i = 0 # 메시지 발행 횟수 카운터

    def timer_callback(self):
        msg = String() # String 메시지 객체 생성
        msg.data = 'Hello World from pyhello!' # 메시지 데이터 설정
        self.publisher_.publish(msg) # 메시지 발행 (ros network에 메세지 전송)
        self.get_logger().info('Publishing: "%s"' % msg.data) # 로그 출력
        self.i += 1 # 발행 횟수 증가

def main(args=None): # ROS python 노드의 표준 main 구조
    rclpy.init(args=args) # ROS2 통신 시스템 초기화 (반드시 실행)
    py_publisher = PyPublisher() # PyPublisher 노드 인스턴스 생성
    rclpy.spin(py_publisher) # 노드가 계속 실행되도록 유지, 콜백 함수가 호출될 때까지 대기
    py_publisher.destroy_node() # 노드 종료 시 자원 정리
    rclpy.shutdown() # ROS2 시스템 종료

if __name__ == '__main__': # 이 파일이 직접 실행될 때 main 함수 호출
    main()