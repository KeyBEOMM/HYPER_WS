cmake_minimum_required(VERSION 3.8)
project(cpphello)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(cpp_receiver src/cpp_receiver.cpp)
ament_target_dependencies(cpp_receiver rclcpp std_msgs)
install(TARGETS
cpp_receiver
DESTINATION lib/${PROJECT_NAME}
)

ament_package()
