from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

HIGH_PRIORITY_PORT = 5001
LOW_PRIORITY_PORT = 5002


def install_flow(connection, out_port, tcp_port, priority):
    msg = of.ofp_flow_mod()
    msg.priority = priority
    msg.match.dl_type = 0x800
    msg.match.nw_proto = 6
    msg.match.tp_dst = tcp_port
    msg.actions.append(of.ofp_action_output(port=out_port))
    connection.send(msg)


def _handle_ConnectionUp(event):
    log.info("Switch connected")

    # High priority traffic
    install_flow(event.connection, 2, HIGH_PRIORITY_PORT, 100)

    # Low priority traffic
    install_flow(event.connection, 2, LOW_PRIORITY_PORT, 10)


def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
