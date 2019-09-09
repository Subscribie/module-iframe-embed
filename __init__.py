from flask import (Blueprint, render_template, abort, request, redirect)
from jinja2 import TemplateNotFound
from subscribie.db import get_jamla
from subscribie.auth import login_required

module_iframe_embed = Blueprint('iframe_embed', __name__, template_folder='templates')

@module_iframe_embed.route('/show-iframe-embed')
@login_required
def get_iframe_embed():
  iframe = '''
        <iframe src={} width="100%" height="800px" scrolling="auto"
                allowfullscreen="true"
                title="Subscription shop">
        </iframe>
        '''.format(request.host_url)
  try:
    return render_template('show-iframe-embed.html', iframe=iframe, jamla=get_jamla())
  except TemplateNotFound:
    abort(404)
