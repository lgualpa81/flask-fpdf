from fpdf import FPDF
import base64
import math
class RPDF(FPDF):
    def __init__(self, orientation="portrait", unit="mm", format="A4", font_cache_dir=True):
        FPDF.__init__(self, orientation="portrait", unit="mm", format="A4", font_cache_dir=True)

    '''
    function Rotate($angle,$x=-1,$y=-1)
    {
        if($x==-1)
            $x=$this->x;
        if($y==-1)
            $y=$this->y;
        if($this->angle!=0)
            $this->_out('Q');
        $this->angle=$angle;
        if($angle!=0)
        {
            $angle*=M_PI/180;
            $c=cos($angle);
            $s=sin($angle);
            $cx=$x*$this->k;
            $cy=($this->h-$y)*$this->k;
            $this->_out(sprintf('q %.5F %.5F %.5F %.5F %.2F %.2F cm 1 0 0 1 %.2F %.2F cm',$c,$s,-$s,$c,$cx,$cy,-$cx,-$cy));
        }
    }
    '''

    def rotation2(self, angle, x=None, y=None):
        """
        This method allows to perform a rotation around a given center.
        The rotation affects all elements which are printed inside the indented context
        (with the exception of clickable areas).
        Args:
            angle (float): angle in degrees
            x (float): abscissa of the center of the rotation
            y (float): ordinate of the center of the rotation
        Notes
        -----
        Only the rendering is altered. The `get_x()` and `get_y()` methods are not
        affected, nor the automatic page break mechanism.
        """
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        if angle == 0:
            self._out("Q\n")
        else:
            angle *= math.pi / 180
            c, s = math.cos(angle), math.sin(angle)
            cx, cy = x * self.k, (self.h - y) * self.k
            s = (
                f"q {c:.5F} {s:.5F} {-s:.5F} {c:.5F} {cx:.2F} {cy:.2F} cm "
                f"1 0 0 1 {-cx:.2F} {-cy:.2F} cm\n"
            )
            self._out(s)
            # yield
            #self._out("Q\n")

pdf = RPDF()
pdf.add_page()
pdf.set_font('Helvetica', '', 16)
pdf.rotation2(90, 50,40)
pdf.cell(40, 10, 'Hello World!',1)
pdf.cell(10, 10, '1!',1)
pdf.rotation2(0)
pdf.set_xy(50,80)
pdf.cell(50, 10, 'hola mundo!',1)

pdf.set_xy(180,260)
pdf.rotation2(90, 180,260)
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(50, 10, 'hola ',1)
pdf.set_font('Helvetica', '', 16)
pdf.cell(50, 10, 'mundo !!!',1)
pdf.output('example1.pdf', 'F')
# pdf_file = pdf.output(dest='S')
# encoded_string = base64.b64encode(pdf_file).decode()
# print(encoded_string)