from supsisim.RCPblk import RCPblk
from scipy import size

def FH_3XXX_ENCBlk(pout, ID, res):
    """

    Call:   FH_3XXX_ENCBlk(pout, ID)

    Parameters
    ----------
       pout: connected output port(s)
       ID : Device ID
       res : Resolution

    Returns
    -------
        blk: RCPblk

    """

    blk = RCPblk('FH_3XXX_ENC',[],pout,[0,0],0,[res],[ID])
    return blk

