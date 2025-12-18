from jinja2 import Environment, FileSystemLoader
import os

from nodeinfo import awsec2
from awsec2 import ec2config  

def render_template_for_node(node, config):
    print("inside render_template_node \n", node)

    print("Node config \n", config)
    """
    Helper function to render the template for a given node.
    """
    node_info = node["awsec2"]
    #print("node_info", node_info)
    template_dir = f'C:\\Users\\user\\Documents\\workspace\\opentofutempletes\\'

    # print("Inside template path", template_file)

    try:
        env = Environment(
            loader=FileSystemLoader(template_dir),
            lstrip_blocks=True,
            trim_blocks=True
        )
        template = env.get_template("awsec2.jinja2")
        #print("Template loaded successfully.", template)
        #print("Node Id:", node_info["id"])
        # Render the template with the node's specific configuration
        service_deploy_config = config.get(node_info["id"])
        #print("service_config", service_deploy_config)
        service_deploy_config["service_id"] = node_info["id"]
        # print("service_deploy_config", service_deploy_config)
        #return template.render(config.get(node["id"]))
        return template.render(service_deploy_config, lstrip_blocks=True, keep_trailing_newline=True)
    except Exception as e:
        print("error occurred in read", e)

result = render_template_for_node(awsec2, ec2config)
#print("Rendered Template:\n", result) 
with open(f".\\templates\\awsec2.tf", 'w') as f:
   f.write(result) 