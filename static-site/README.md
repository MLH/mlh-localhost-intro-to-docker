# Docker Static Site

This is a fork of the [Docker Static Site example][1] for MLH Localhost Intro
to Docker workshops.

## Running the Example

This example is host on DockerHub as [mlhacks/docker-static-site][3].  You can download
and run it locally with the following command:

```
$ docker run -d -p 8888:80 mlhacks/docker-static-site
```

## Building the Example

To run this example, you need to build the Docker Image first. To do so, run
the following command:

```
$ docker build -t docker-static-site .
```

After you've built the image, you can run it as follows:

```
$ docker run -d -p 8888:80 docker-static-site
```

The website should now be accessible at [http://localhost:8888/][2].

## License

The original code was released under the Apache License 2.0 by Docker, Inc.
That license is included with this code in the [LICENSE](LICENSE) file.

The modifications to this code are released under the MIT License, copyright 
Major League Hacking, Inc ([READ LICENSE](../README.md)).

[1]: https://github.com/docker/labs/tree/master/beginner/static-site
[2]: http://localhost:8888
[3]: https://hub.docker.com/r/mlhacks/docker-static-site/
