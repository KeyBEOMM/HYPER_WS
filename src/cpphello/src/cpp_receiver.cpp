#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class CppSubscriber : public rclcpp::Node
{
public:
    // constructor - inherit Node class 
    CppSubscriber() : Node("cpp_subscriber") {
        // subscriber options - topic name(subscription), queue size(10), callback function(std::bind)
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "hello_topic", // topic name
            10, // queue size
            std::bind(&CppSubscriber::topic_callback, this, std::placeholders::_1) // callback function
            // std::bind - bind the callback function to the subscriber, this is a common way to use member functions as callbacks in C++
            // std::bind parameters:
            // 1) callback function (topic_callback) -> pointer of function / format : &클래스이름::함수이름
            // 2) object pointer (this) -> pointer of object(누구의 함수인지) / format : this
            // 3) placeholders for arguments (std::placeholders::_1) -> where to put the received message / format : std::placeholders::_1
        );
  }
private:
    // callback function topic_callback(std::bind로 전달받은 메시지)
    void topic_callback(const std_msgs::msg::String::SharedPtr msg) const { 
        // RCLCPP_INFO is a macro provided by the ROS 2 C++ client library (rclcpp) for logging informational messages.
        // RCLCPP_INFO parameters: 
        // 1) logger - this->get_logger() -> get the logger associated with this node, which allows you to log messages that are tagged with the node's name.
        // 2) format string (similar to printf-style formatting), 
        // 3) additional arguments (in this case, the data from the received message).
        RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
    }
    // subscriber object : object that assign subscription variable made by create_subscription function 
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char * argv[]) {
    // ROS2 intialization
    rclcpp::init(argc, argv);

    // run the subscriber node : create an instance of the CppSubscriber class and pass it to rclcpp::spin, which will keep the node alive and processing callbacks until it is shut down.
    rclcpp::spin(std::make_shared<CppSubscriber>());

    // shutdown the ROS 2 system
    rclcpp::shutdown();
    return 0;
}