list = ["python", "django", "docker", "drf"]

match list:
    case ["python", "django"]:
        print("python and django")
    case ["django", "docker"]:
        print("django and docker")
    case ["docker", "drf"]:
        print("docker and drf")
    case ["python", "django", "docker", "drf"]:
        print("All Courses selected")
    case _:
        print("No Course selected")
