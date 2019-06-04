import eventlet

eventlet.monkey_patch()

import logging
import sys

log = logging.getLogger()
log.addHandler(logging.StreamHandler(sys.stderr))
log.setLevel(logging.DEBUG)

from ryu.services.protocols.bgp.bgpspeaker import BGPSpeaker

def dump_remote_best_path_change(event):
    print 'the best path changed:', event.remote_as, event.prefix,\
        event.nexthop, event.is_withdraw

def detect_peer_down(remote_ip, remote_as):
    print 'Peer down:', remote_ip, remote_as


SSH = {
    'ssh_port': 4990,
    'ssh_host': 'localhost',
    'ssh_host_key': '/etc/ssh_host_rsa_key',
    'ssh_username': 'ryu',
    'ssh_password': 'ryu',
}

if __name__ == "__main__":
    speaker = BGPSpeaker(as_number=65005, router_id='172.16.1.174',
                         best_path_change_handler=dump_remote_best_path_change,
                         peer_down_handler=detect_peer_down)

   

