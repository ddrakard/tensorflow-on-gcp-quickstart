# Quick start guide for Vertex AI

1. You must have an account on Google Cloud Platform with Artifact Registry and
   Vertex AI enabled.
2. You must have [Docker](https://www.docker.com/) installed.
3. Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
   on your computer.
4. Download this project.
5. It is strongly recommended that you use a python virtual environment like
   [venv](https://docs.python.org/3/library/venv.html). You can see
   [this guide](setting-up-venv.md) for instructions.
6. Write your Python code inside this project. It is recommended to use the
   convention where you put your source files inside a Python
   [package](https://docs.python.org/3/tutorial/modules.html) directory under
   the root of this project. Your code should automatically upload the trained
   model to accessible location, because you will not be able to access any 
   files in the project when it is running on the Vertex AI platform. If you
   will run a long or expensive job, it is suggested it uploads model snapshots
   regularly during training.
7. Update the `setup.py` file in this project's base directory to include all
   the dependencies you need. To avoid errors, make sure you install
   dependencies only using the setup.py and not separately. To install
   dependencies you have listed in `setup.py`, you can run the command
   `pip3 install --editable .` (only recommended if you are using a virtual
   environment).
8. When your project is finished and working locally, update the last lines of
   the dockerfile `execution/build_vertex_ai_docker_image/Dockerfile` to run
   the command you use to execute your code.
9. Build the docker image by running
   `execution/build_vertex_ai_docker_image/build_docker.sh`. This should finish
   with an output telling you the hash of the build image, something like:
  `=> => writing image sha256:5cab90d5215b14603162c5b31071ea4fe48a841cbe5c30ff9c6a125e77fd4d69`
10. Create a repository in your GCP Artifact Registry for your Docker image, if
    you don't already have one.
11. Run `gcloud auth application-default login` on your computer to grant
    yourself access to your Artifact Registry.
12. You must know your Artifact Registry location code, project ID, and
    repository name. These are shown on your repository page in GCP. For
    example `us-docker.pkg.dev > my-project > docker-images`
    indicates location: `us`, project: `my-project`,  repository:
    `docker-images`.
13. Run the command `gcloud auth configure-docker ` followed by the location
    hostname, for example `gcloud auth configure-docker  us-docker.pkg.dev`.
14. Tag your image. This is the command:
     
    `docker tag `*image hash*` `*location*`-docker.pkg.dev/`*project
    ID*`/`*repository name*`/`*image name*
    
    The image name can be any name you choose. Following the examples above,
    this would be:
    
    `docker tag 5cab90d5215b14603162c5b31071ea4fe48a841cbe5c30ff9c6a125e77fd4d69 us-docker.pkg.dev/my-project/docker-images/my-vertex-job`

15. Push your image to your the Artifact Registry. For example:

    `docker push us-docker.pkg.dev/my-project/docker-images/my-vertex-job`

17. Click the `Create` button in the Training tab of Vertex AI in Google Cloud
    Platform.
17. In the Train New Model panel that appears:
    1. In the `Training method` stage, enter the following fields: Dataset:
       `No managed dataset`, Annotation set: `-`, Objective: `Custom`. Click
       the `Custom training (advanced)` option, then click the `CONTINUE`
       button.
    2. In the `Model details` stage, enter a name of your choice for the job
       in the `model name` field then click the `CONTINUE` button.
    3. In the `Training container` stage, click the `Custom container` option,
       then click the `BROWSE` link in the `Container image` field, and choose
       the container you uploaded earlier, then click the `CONTINUE` button.
    4. In the `Hyperparameters` stage, click the `CONTINUE` button.
    5. In the `Compute and pricing` stage, enter the details of the harware you
       would like, then click the `START TRAINING` button.
