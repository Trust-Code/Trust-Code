# -*- encoding: utf-8 -*-

from tools.translate import _
from report import report_sxw
from report.report_sxw import rml_parse
import locale

class Parser(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'for_numb':self.for_numb,
        })

    def  for_numb(self, vlr, lang):
        
        locale.setlocale(locale.LC_ALL, (lang,'UTF-8'))
        vlr = locale.format('%1.2f', vlr, 2)
        
        return vlr
