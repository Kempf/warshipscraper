import pandas as pd
import re
import math

# ISO 3166 ALPHA-3 codes are used
def country_sort(s):
    if isinstance(s, str):
        # aus
        if re.search(r'\bhmas\b|australia|\bran\b|H\.M\.A\.S\.|hma ship',s,flags=re.IGNORECASE):
            return 'aus'
        # can
        if re.search(r'\b(hmcs|rcn)\b|canad|H\.M\.C\.S\.',s,flags=re.IGNORECASE):
            return 'can'
        # rus
        if re.search(r'\b(vmf)\b|\brussia|\bsoviet|\bussr\b|\bmoskva|\bkirov|\budaloy|\bsovreme|\bstereg|\bkuznet|typhoon|borei|akula|yasen|\bkilo[\b-]|\bslava|\bproject|\bBuyan|\bKalibr|Kiev',s,flags=re.IGNORECASE):
            return 'rus'  
        # ger
        if re.search(r'\bgerm|kr(ie|ei)gsmarine|\bsms\b|\bDKM\b|U-\d\d\d|Scharnhorst|Bismarck|hamburg|S\.M\.S\.|U-boat|graf spee',s,flags=re.IGNORECASE):
            return 'deu'
        # ita
        if re.search(r'\bital|\bITS\b',s,flags=re.IGNORECASE):
            return 'ita'
        # jap
        if re.search(r'\bjapa|\bIJN\b|JMSDF\b|marit.*self.*def|\bjs\b|yamato|jds|Musashi',s,flags=re.IGNORECASE):
            return 'jpn'
        # nl
        if re.search(r'\bdutch|\bhnlms\b|Zr\.[\s]Ms\.|Nederland|Netherlands',s,flags=re.IGNORECASE):
            return 'nld'
        # fra
        if re.search(r'\bfren|\bfranc|\bfs\b|\bCDG\b|Charles de Gaulle|Aquitaine',s,flags=re.IGNORECASE):
            return 'fra'
        # swe
        if re.search(r'\bswed|\bhswms|\bkms|visby',s,flags=re.IGNORECASE):
            return 'swe'
        # dan
        if re.search(r'\bdani|\bdenma|\bhdms',s,flags=re.IGNORECASE):
            return 'dnk'
        # chi
        if re.search(r'\bchin|\bplan|\bpeople.*army.*liberation|PLA Navy',s,flags=re.IGNORECASE):
            return 'chn'
        # nor
        if re.search(r'\bnorw|\bknm\b|\bhnoms\b',s,flags=re.IGNORECASE):
            return 'nor'
        # nz
        if re.search(r'\bnew ze|\bhmnzs\b',s,flags=re.IGNORECASE):
            return 'nzl'
        # spa
        if re.search(r'\besps\b|\bspan|\barmada|\bspain',s,flags=re.IGNORECASE):
            return 'esp'
        # kor
        if re.search(r'\bROKN\b|\bkorea|\bROK\b|\bROKS\b',s,flags=re.IGNORECASE):
            return 'kor'
        # tur
        if re.search(r'\bturk|\bTCG',s,flags=re.IGNORECASE):
            return 'tur'
        # indonesia
        if re.search(r'\bKRI\b|\bindon',s,flags=re.IGNORECASE):
            return 'idn'
        # greece
        if re.search(r'\bhellen|\bgreek|\bgreece',s,flags=re.IGNORECASE):
            return 'grc'
        # argenti
        if re.search(r'\bARA\b|\bargenti',s,flags=re.IGNORECASE):
            return 'arg'
        # peru
        if re.search(r'\bBAP\b|\bperu',s,flags=re.IGNORECASE):
            return 'per'
        # braz
        if re.search(r'\bphm\b|\bbraz',s,flags=re.IGNORECASE):
            return 'bra'
        # fin
        if re.search(r'\bfinn|\bfinla',s,flags=re.IGNORECASE):
            return 'fin'
        # india
        if re.search(r'\bins\b|\bindia',s,flags=re.IGNORECASE):
            return 'ind'
        # israel
        if re.search(r'\bisrae|\bINS\b',s,flags=re.IGNORECASE):
            return 'isr'
        # portuga
        if re.search(r'\bportug|\bnrp\b',s,flags=re.IGNORECASE):
            return 'prt'
        # singap
        if re.search(r'\bRSS\b|Singapo',s,flags=re.IGNORECASE):
            return 'sgp'
        # malay
        if re.search(r'\bMalay|\bRMN|\bTLDM|\bKD\b',s,flags=re.IGNORECASE):
            return 'mys'
        # colomb
        if re.search(r'\bARC|\bcolomb',s,flags=re.IGNORECASE):
            return 'col'
        # irela
        if re.search(r'\bL[EÉ]\b|Irela|Irish',s,flags=re.IGNORECASE):
            return 'irl'
        # egypt
        if re.search(r'\bEgypt',s,flags=re.IGNORECASE):
            return 'egy'
        # roma
        if re.search(r'\bRomania',s,flags=re.IGNORECASE):
            return 'rou'
        # croat
        if re.search(r'\bCroat',s,flags=re.IGNORECASE):
            return 'hrv'
        # iran
        if re.search(r'\bIrani',s,flags=re.IGNORECASE):
            return 'irn'
        # thai
        if re.search(r'\bThai|\bHMTS',s,flags=re.IGNORECASE):
            return 'tha'
        # algeria
        if re.search(r'\bAlgeria',s,flags=re.IGNORECASE):
            return 'dza'
        # bangla
        if re.search(r'\bBanglad|\bBNS\b',s,flags=re.IGNORECASE):
            return 'bgd'
        # bru
        if re.search(r'\bBrunei',s,flags=re.IGNORECASE):
            return 'brn'
        # chil
        if re.search(r'\bChile',s,flags=re.IGNORECASE):
            return 'chl'
        # ecuad
        if re.search(r'\bEcuad',s,flags=re.IGNORECASE):
            return 'ecu'
        # estonia
        if re.search(r'\bEstonia',s,flags=re.IGNORECASE):
            return 'est'
        # ukraine
        if re.search(r'\bUkrain',s,flags=re.IGNORECASE):
            return 'ukr'
        # ukraine
        if re.search(r'\bUrug',s,flags=re.IGNORECASE):
            return 'ury'
        # viet
        if re.search(r'\bVietnames',s,flags=re.IGNORECASE):
            return 'vnm'
        # uk
        if re.search(r'\b(hms|rfa|rn)\b|british|(her|his) maj(((?!aust)(?!canad)(?!new)).)*$|royal navy|H\.M\.S\.|hm ship|english|queen elizabeth|\bQE\b|\bNelson',s,flags=re.IGNORECASE):
            return 'gbr'
        # usa
        if re.search(r'\b(uss|us|usns|usn)\b|U[\b\.]S[\.]|\bUSCG|DD[-\s]\d\d\d|BB[-\s]\d\d|CV[NL]*[-\s]\d\d|Iowa|texas|USGCC|virginia|los angeles|C[AL]-\d\d|Arleigh Burke|United States|Zumwalt|Washington|SSN[-\s]\d\d\d|New Jersey|Vietnam',s,flags=re.IGNORECASE):
            return 'usa'
    return ''

# load stripped titles file    
t = pd.read_csv('titles.csv',index_col=0)
# apply country sort
t['country']=t.title.apply(country_sort)

# save sorted and unsorted lists
t[t.country==''].title.to_csv('titles_unsorted.csv')
t.to_csv('titles_sorted.csv')