# Quick start guide for a graphical virtual workstation


Be aware that you will be charged for your GPU all the time your virtual
workstation is running (even if it is not executing code, and you are just
writing code or pondering), so it can be more cost-effective to use batch jobs
on Vertex AI if you want very powerful hardware.

**Remember to shut down your workstation at the end of your session to avoid
extra costs!**

This guide uses Chrome remote desktop. It does not require you to install
anything on your local computer to connect to the virtual workstation (apart
from Chrome / Chromium web browser with no extra plugins needed).

1. In the VM Instances panel of Compute Engine in Google Cloud Platform click
   the `CREATE INSTANCE` button.
2. In the New VM Instance page, click the `CHANGE` button in the `Boot disk`
   section.
3. In the Boot disk panel, enter `Deep Learning on Linux` for the Operating
   System. Choose an appropriate `Version` option. It should include "CUDA"
   (the GPU graphics driver). At the time of writing
   `Deep Learning Image: TensorFlow Enterprise 2.6 m80 CUDA 110` is probably
   the best option. It is stronly recommended that you choose an SSD disk for
   the Boot disk type. Finally press the `SELECT` button.
4. Fill out your remaining specification requirements for the workstation. You
   do not need to enable NVIDIA GRID. Then click the `CREATE` button.
5. On the VM Instances page click the `SSH` link on the newly created instance
   to open the SSH shell.
6. There should be a prompt on the command line asking if you wish to install
   the GPU driver. Confirm this and check that the install completes
   successfully. Sometimes the package manager is busy for a while after the
   vm starts so you will need to wait briefly before you confirm.
7. Set a password and sudo permissions for the current user. The automatic
   permissions will not work when accessing the workstation on the graphical
   desktop. User the `sudo passwd $USER` and `sudo usermod -aG sudo $USER`
   commands. If you do not know the current username, run the `whoami` command
   to find out.
8. Restart the VM so it connects to remote desktop with the correct hostname.
9. Follow the instructions on this page
   https://cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine
   starting from the section "Installing Chrome Remote Desktop on the VM
   instance". You should now be able to connect to the graphical desktop.

### Optional

10. Install Snap for software like PyCharm: `sudo apt install snapd`.
11. Install the PyCharm IDE: `sudo snap install pycharm-community --classic`.
12. Restart the VM so the PyCharm icon appears in the system menu.

### Running in docker

13. The procedure above should give you a workstation correctly configured to
    run Tensorflow with GPU acceleration. However Tensorflow GPU setup is quite
    fragile, and if you encounter problems or you wish to run your code on a
    different system, you may wish to run in a Docker container. This only
    requires basic GPU drivers (not CUDA and fragile version compatibility) on
    the host system. To do so continue the instructions.
14. Ensure [Docker](https://www.docker.com/) is installed.
15. Download this project onto the workstation.
16. It is strongly recommended that you use a python virtual environment like
   [venv](https://docs.python.org/3/library/venv.html). You can see
   [this guide](setting-up-venv.md) for instructions.
17. Write your Python code inside this project. It is recommended to use the
   convention where you put your source files inside a Python
   [package](https://docs.python.org/3/tutorial/modules.html) directory under
   the root of this project.
18. Update the `setup.py` file in this project's base directory to include all
   the dependencies you need. To avoid errors, make sure you install
   dependencies only using the setup.py and not separately. To install
   dependencies you have listed in `setup.py`, you can run the command
   `pip3 install --editable .` (only recommended if you are using a virtual
   environment).
19. Run `execution/run_in_docker_gpu.sh`
