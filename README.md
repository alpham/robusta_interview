
# robusta Interview
This repo is created as part of interviewing with [robusta](https://robustastudio.com/) company.

Usage

1. Install the requirements

    $ pip3 install requirements

2. Start using the command line

    $ python3 ./cipher.py --help
    Usage: cipher.py [OPTIONS] TEXT...
    
    Options:
      -a, --algorithm TEXT  Which algorithm to use ( available ~> shift, matrix )
                            [required]
      -m, --method TEXT     Which method to run (encode, decode)  [required]
      --help                Show this message and exit.

Or using the docker file

1. Build docker image

    $ docker build -t cipher_cli .

2. Start using the application

    $ docker run -it --rm cipher_cli --help
