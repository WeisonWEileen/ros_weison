#include "ros/ros.h"
#include "actionlib/server/simple_action_server.h"
#include "demo_action/AddIntsAction.h"


typedef actionlib::SimpleActionServer<demo_action::AddIntsAction> Server;
int main(int argc, char *argv[])
{
    ros::init(argc, argv, "addInts_server");
    ros::NodeHandle nh;
    // Server server(nh, "addInts", ,false);
    // server.start();
    
    
    
    return 0; 
}
