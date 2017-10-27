import os
import logging
import logging.handlers
import subprocess

from flask import Flask, request, abort, jsonify

VERSION = '1.0.0'
app = Flask(__name__)
DEFAULT_BASE_DIR = "/home/admin/conf/ansible_playbooks/"
DEFAULT_REPOSITORY = "ALL_REPOSITORIES"
DEFAULT_BRANCH = "origin/develop"
LOGGER_PATH = "/home/admin/conf/ansible_playbooks/logs"


def init_logger(path):
    log_formatter = "%(asctime)s | %(levelname)s - %(message)s"
    date_formatter = "%Y-%m-%d %H:%M:%S"
    if isinstance(path, str) and os.path.exists(os.path.dirname(path)):
        log = logging.getLogger('ansible-api-%s' % VERSION)
        logHandler = logging.handlers.TimedRotatingFileHandler(path, when='midnight')
        logFormatter = logging.Formatter(fmt=log_formatter, datefmt=date_formatter)
        logHandler.setFormatter(logFormatter)
        log.addHandler(logHandler)
        log.setLevel(logging.DEBUG)
        log.propagate = False  # disable console output
    else:
        logging.basicConfig(level=logging.DEBUG,
                            format=log_formatter, datefmt=date_formatter)
        log = logging.getLogger('ansible-api-%s' % VERSION)
    return log


LOGGER = init_logger(LOGGER_PATH)


@app.errorhandler(400)
def type_error():
    resp = {"error": True, "msg": "Request header or json data error."}
    return jsonify(resp), 400


@app.route("/gitpull", methods=['POST'])
def handle_request():
    if request.headers.get('Content-Type') != "application/json":
        abort(400)
    # user_data = json.loads(request.get_data())

    base_dir = request.args.get('basedir', DEFAULT_BASE_DIR)
    repository = request.args.get('repository', DEFAULT_REPOSITORY)
    branch = request.args.get('branch', DEFAULT_BRANCH)

    LOGGER.info("basedir: " + base_dir)
    LOGGER.info("repository: " + repository)

    try:
        result = git_pull(base_dir, repository, branch)
        resp = {"msg": result}
        return jsonify(resp), 200

    except Exception as e:
        resp = {"error": True, "msg": str(e)}
        return jsonify(resp), 444


def git_pull(base_dir, repository, branch):
    if not os.path.isdir(base_dir):
        raise Exception("can not find dir " + base_dir)
    repos_dir = []
    if repository == DEFAULT_REPOSITORY:
        repos = os.listdir(base_dir)
        for rep in repos:
            rep_dir = os.path.join(base_dir, rep)
            if os.path.isdir(rep_dir):
                repos_dir.append(rep_dir)
    else:
        repos_dir.append(os.path.join(base_dir, repository))

    results = []
    for repos in repos_dir:
        p = subprocess.Popen('cd %s && git fetch --all && git reset --hard %s' % (repos, branch), shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        r = {"stdout": p.stdout.read()}
        LOGGER.info(str(r))
        results.append({repos: r})
    LOGGER.info(results)
    return results


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)
