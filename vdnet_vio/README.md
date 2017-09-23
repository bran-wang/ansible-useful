1. use you vdnet jumphost IP to replace inventory host

2. use command line to pass vdnet_ip variables
> ansible-playbook -i inventory setup_vdnet_vio.yml -e "vdnet_ip=$your_jumphost_ip"
