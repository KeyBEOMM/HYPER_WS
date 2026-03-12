cmake_minimum_required(VERSION 3.8)
project(cpp_pkg1)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(cpp_node1 src/cpp_node1.cpp)
ament_target_dependencies(cpp_node1 rclcpp std_msgs)

install(TARGETS
cpp_node1
DESTINATION lib/${PROJECT_NAME}
)

ament_package()