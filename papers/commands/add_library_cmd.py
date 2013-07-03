from .. import repo
from ..paper import Paper
from ..configs import config

def parser(subparsers):
    parser = subparsers.add_parser('add_library',
            help='add a set of papers to the repository')
    parser.add_argument('bibfile', help='bibtex, bibtexml or bibyaml file')
    return parser


def command(args):
    """
    :param bibfile       bibtex file (in .bib, .bibml or .yaml format.
    """

    ui = args.ui
    bibfile = args.bibfile

    rp = repo.Repository(config())
    for p in Paper.many_from_bib(bibfile):
        rp.add_paper(p)
