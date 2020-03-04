from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Flowable, Image
from reportlab.lib.styles import (ParagraphStyle, getSampleStyleSheet)
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from datetime import datetime
class MCLine(Flowable):
    """
    Line flowable --- draws a line in a flowable
    http://two.pairlist.net/pipermail/reportlab-users/2005-February/003695.html
    """
    #----------------------------------------------------------------------
    def __init__(self, width, height=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height
    #----------------------------------------------------------------------
    def __repr__(self):
        return "Line(w=%s)" % self.width
    #----------------------------------------------------------------------
    def draw(self):
        """
        draw the line
        """
        self.canv.line(0, self.height, self.width, self.height)
def fel_build(data):
    if data[4] == 1:
        perm = "Ja"
    else:
        perm = "Nej"
    content = [
        ["Address", data[0]],
        ["Namn", data[1]],
        ["LGHNR", data[2]],
        ["Datum", data[3]],
        ["Tillträde", perm]
    ]


    styles = getSampleStyleSheet()
    table = Table(content, colWidths=[125, '*'])
    # add style
    style = TableStyle([
        ('TEXTCOLOR',(0,0),(-1,0),colors.black),

        ('ALIGN',(0,0),(-1,-1),'LEFT'),

        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 12),

        ('BOTTOMPADDING', (0,0), (-1,0), 5),
        ('LEFTPADDING', (0,0), (-1,0), 5),
        ('BACKGROUND',(0,1),(-1,-1),colors.white),
    ])
    table.setStyle(style)
    ts = TableStyle(
        [
        ('BOX',(0,0),(0,0),1,colors.white),


        ('GRID',(0,1),(-1,-1),1,colors.gray),
        ]
    )
    table.setStyle(ts)
    elems = []
    hStyle = ParagraphStyle("asdf",
                   fontName="Helvetica-Bold",
                   fontSize=20,
                   parent=styles['Heading2'],
                   alignment=0,
                   spaceAfter=50)

    header = Paragraph("Felanmälan", style=hStyle)
    elems.append(header)
    elems.append(table)
    style = getSampleStyleSheet()
    paraStyle = ParagraphStyle("asdf",
                   fontName="Helvetica",
                   fontSize=10,
                   parent=styles['Heading2'],
                   alignment=0,
                   spaceAfter=0)
    pStyle = ParagraphStyle("asdf",
                   fontName="Helvetica-bold",
                   fontSize=11,
                   borderWidth=1,
                   leading=15,
                   borderColor=colors.gray,
                   parent=styles['Heading2'],
                   alignment=1,
                   spaceBefore=25,
                   spaceAfter=15)
    li = MCLine(500)
    p_title = Paragraph("Beskrivning", style=pStyle)
    para = Paragraph(data[6], style=paraStyle)

    elems.append(p_title)
    elems.append(para)

    return elems
def int_build(data):

    content = [
        ["Address", data[0]],
        ["Namn", data[1]],
        ["LGHNR", data[2]],
        ["Datum", data[3]]
    ]

    styles = getSampleStyleSheet()
    table = Table(content, colWidths=[125, '*'])
    # add style
    style = TableStyle([
        ('TEXTCOLOR',(0,0),(-1,0),colors.black),

        ('ALIGN',(0,0),(-1,-1),'LEFT'),

        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 12),

        ('BOTTOMPADDING', (0,0), (-1,0), 5),
        ('LEFTPADDING', (0,0), (-1,0), 5),
        ('BACKGROUND',(0,1),(-1,-1),colors.white),
    ])
    table.setStyle(style)
    ts = TableStyle(
        [
        ('BOX',(0,0),(0,0),1,colors.white),


        ('GRID',(0,1),(-1,-1),1,colors.gray),
        ]
    )
    table.setStyle(ts)
    elems = []
    hStyle = ParagraphStyle("asdf",
                   fontName="Helvetica-Bold",
                   fontSize=20,
                   parent=styles['Heading2'],
                   alignment=0,
                   spaceAfter=50)

    header = Paragraph("Intresseanmälan", style=hStyle)
    elems.append(header)
    elems.append(table)
    style = getSampleStyleSheet()
    paraStyle = ParagraphStyle("asdf",
                   fontName="Helvetica",
                   fontSize=10,
                   parent=styles['Heading2'],
                   alignment=0,
                   spaceAfter=0)
    pStyle = ParagraphStyle("asdf",
                   fontName="Helvetica-bold",
                   fontSize=11,
                   borderWidth=1,
                   leading=15,
                   borderColor=colors.gray,
                   parent=styles['Heading2'],
                   alignment=1,
                   spaceBefore=25,
                   spaceAfter=15)
    li = MCLine(500)
    p_title = Paragraph("Meddelande", style=pStyle)
    para = Paragraph(data[6], style=paraStyle)

    elems.append(p_title)
    elems.append(para)

    return elems
def create_pdf(adr, name, lghnr, date, access, cat, largeText, type):
    fileName = 'pdf/{0}-{2}-{1}-ny.pdf'.format(type, datetime.today().strftime('%Y%m%d%H%I%S'), name.replace(" ", "_").lower())
    pdf = SimpleDocTemplate(
    fileName,
    pagesize=letter
    )
    # Configurations
    data = [adr, name, lghnr, date, access, cat, largeText]
    pdf.build(fel_build(data))
