from kobozo_crossplane.common.analyzer import register_external_directives
from kobozo_crossplane.helpers.lexer import register_external_lexer
from kobozo_crossplane.nginx_dumper import register_external_builder
from kobozo_crossplane.nginx_parser import register_external_parser


class CrossplaneExtension:
    directives = {}

    def register_extension(self):
        register_external_directives(directive=self.directives)
        register_external_lexer(directives=self.directives, lexer=self.lex)
        register_external_parser(directives=self.directives, parser=self.parse)
        register_external_builder(directives=self.directives, builder=self.build)

    def lex(self, token_iterator, directive):
        raise NotImplementedError

    def parse(self, stmt, parsing, tokens, ctx=(), consume=False):
        raise NotImplementedError

    def build(self, stmt, padding, state, indent=4, tabs=False):
        raise NotImplementedError
