cd -P -- "$(dirname -- "$0")" # Set the working directory to the script directory
DOCKER_BUILDKIT=1 docker build ../.. -f Dockerfile