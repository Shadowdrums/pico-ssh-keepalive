# pico-ssh-keepalive
this is a simple keep alive for pico to keep ssh server connection up.

# Raspberry Pico W Router Connection Assistant 🌐

Maintain persistent SSH connections to your Raspberry Pi 4 servers with the Raspberry Pico W, crafted to flawlessly interface with a router developed from a Raspberry Pi 4.

## 🌟 Overview

This MicroPython script is engineered for the **Raspberry Pico W** microcontroller. Its primary objective is to guarantee the SSH connections to two Raspberry Pi 4 servers stay active, facilitating seamless remote access both locally and from outside the network.

## 🛠 Setup

### Prerequisites

1. **Raspberry Pico W** microcontroller board.
2. [Thonny IDE](https://thonny.org/): An integrated development environment for Python that supports MicroPython. We utilize Thonny to craft, modify, and directly upload our MicroPython scripts to the Raspberry Pico W.
3. An operational network stemming from a Raspberry Pi 4-based router, equipped with relevant network credentials (SSID and Password).

### Installation and Deployment

1. Connect your Raspberry Pico W to your workstation.
2. Launch [Thonny IDE](https://thonny.org/) and designate the Raspberry Pico W as the target interpreter.
3. Transfer this script onto the Raspberry Pico W.
4. Make sure the network identifiers in the script (`Network_name` and `Network_password`) are congruent with your Raspberry Pi 4 router's credentials. Note: `Network_name` refers to the SSID of the router your servers are connected to, while `Network_password` is the router's password. Modify these values accordingly in the script.
5. Replace the placeholders `server_ip1` and `server_ip2` with the actual local IPs of your primary and secondary Raspberry Pi 4 servers.
6. Deploy the script. LED indicators provide visual feedback concerning the connection's status.

## 📈 Functionality

1. **LED Indicators**: Upon successful network connection, the onboard LED will flash thrice. Subsequent single flashes indicate ping attempts to the servers.
2. **Main Loop**:
    - Induces a 2-minute sleep cycle.
    - Post-sleep, the system endeavors to sustain SSH connections to two server IPs (`server_ip1` and `server_ip2`).
    - The onboard LED provides feedback during each connection trial. A consistent LED illumination signifies a successful connection.

3. **Purpose**:
    - The script is crucial for keeping the SSH connection alive, ensuring that users can seamlessly remote in, both from an external network (to `server_ip1` as this is the primary server with outside network port forwarding enabled) and from within the local network (to both servers).
    - Note: While `server_ip1` is configured for both local and external SSH access, `server_ip2` is tailored exclusively for local SSH access.

## 💡 Conclusion

The **Raspberry Pico W Router Connection Assistant** epitomizes the robustness and versatility of the Raspberry Pico W when meshed with the Raspberry Pi 4 ecosystem. Whether you're helming a sophisticated homelab, executing pivotal services, or merely navigating the expansive domain of microcomputing, this tool offers unparalleled reliability.

---

**Forge Ahead into the World of Connected Computing!** 🚀
