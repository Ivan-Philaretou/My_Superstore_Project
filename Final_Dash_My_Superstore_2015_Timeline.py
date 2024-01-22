
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc

df_1 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/1_Superstore_Datamart_2015_Modified_v2.csv')
df_2 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/2_Superstore_Datamart_2015_Modified_v2.csv')
df_3 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/3_Superstore_Datamart_2015_Modified_v2.csv')

full_df = pd.concat([df_1,df_2,df_3])
df = full_df

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

# Heading
header  = html.Div([ html.Div(
        className="app-header",
        children=[
            html.H2('Superstore Timeline Data',
                     className="app-header--title",
                     style={'text-align': 'center'})])
        ]
    )

# Filters
side = html.Div([
    html.Center(
        children=html.Div([
            html.H3('Brand Name Filter:')
        ], style = {'padding-bottom': '5px', 'width': '90%', "padding-top": "5px"})
    ),
    html.Center(dcc.Dropdown(
        id='brand_name_option',
        options=[
            {'label': 'APC', 'value': 'APC'},
            {'label': 'AT&T', 'value': 'AT&T'},
            {'label': 'Aastra', 'value': 'Aastra'},
            {'label': 'Acco', 'value': 'Acco'},
            {'label': 'Acme', 'value': 'Acme'},
            {'label': 'Adams', 'value': 'Adams'},
            {'label': 'Adjustable', 'value': 'Adjustable'},
            {'label': 'Adtran', 'value': 'Adtran'},
            {'label': 'Advantus', 'value': 'Advantus'},
            {'label': 'Akro', 'value': 'Akro'},
            {'label': 'Alliance', 'value': 'Alliance'},
            {'label': 'Aluminum', 'value': 'Aluminum'},
            {'label': 'Amazon', 'value': 'Amazon'},
            {'label': 'Ampad', 'value': 'Ampad'},
            {'label': 'Anderson Hickey Conga', 'value': 'Anderson Hickey Conga'},
            {'label': 'Angle', 'value': 'Angle'},
            {'label': 'Anker', 'value': 'Anker'},
            {'label': 'Apple', 'value': 'Apple'},
            {'label': 'Arkon', 'value': 'Arkon'},
            {'label': 'Array', 'value': 'Array'},
            {'label': 'Artistic', 'value': 'Artistic'},
            {'label': 'Assorted', 'value': 'Assorted'},
            {'label': 'Astroparche', 'value': 'Astroparche'},
            {'label': 'Ativa', 'value': 'Ativa'},
            {'label': 'Atlantic Metals', 'value': 'Atlantic Metals'},
            {'label': 'Avanti', 'value': 'Avanti'},
            {'label': 'Avaya', 'value': 'Avaya'},
            {'label': 'Avery', 'value': 'Avery'},
            {'label': 'BIC', 'value': 'BIC'},
            {'label': 'BPI', 'value': 'BPI'},
            {'label': 'Balt', 'value': 'Balt'},
            {'label': 'Barricks', 'value': 'Barricks'},
            {'label': 'Belkin', 'value': 'Belkin'},
            {'label': 'Berol', 'value': 'Berol'},
            {'label': 'Bestar', 'value': 'Bestar'},
            {'label': 'Bevis', 'value': 'Bevis'},
            {'label': 'Binney & Smith', 'value': 'Binney & Smith'},
            {'label': 'Bionaire', 'value': 'Bionaire'},
            {'label': 'Black', 'value': 'Black'},
            {'label': 'Black & Decker', 'value': 'Black & Decker'},
            {'label': 'Black Berry', 'value': 'Black Berry'},
            {'label': 'Blue', 'value': 'Blue'},
            {'label': 'Bose', 'value': 'Bose'},
            {'label': 'Boston', 'value': 'Boston'},
            {'label': 'Bravo', 'value': 'Bravo'},
            {'label': 'Bretford', 'value': 'Bretford'},
            {'label': 'Brites', 'value': 'Brites'},
            {'label': 'Brother', 'value': 'Brother'},
            {'label': 'Brown', 'value': 'Brown'},
            {'label': 'Bulldog', 'value': 'Bulldog'},
            {'label': 'Bush', 'value': 'Bush'},
            {'label': 'C-Line', 'value': 'C-Line'},
            {'label': 'Cameo', 'value': 'Cameo'},
            {'label': 'Canon', 'value': 'Canon'},
            {'label': 'Canvas', 'value': 'Canvas'},
            {'label': 'Cardinal', 'value': 'Cardinal'},
            {'label': 'Career', 'value': 'Career'},
            {'label': 'Carina', 'value': 'Carina'},
            {'label': 'Case', 'value': 'Case'},
            {'label': 'Catalog', 'value': 'Catalog'},
            {'label': 'Central Association', 'value': 'Central Association'},
            {'label': 'Cherry', 'value': 'Cherry'},
            {'label': 'Chroma Craft', 'value': 'Chroma Craft'},
            {'label': 'Chromcraft', 'value': 'Chromcraft'},
            {'label': 'Cisco', 'value': 'Cisco'},
            {'label': 'Clarity', 'value': 'Clarity'},
            {'label': 'Classic', 'value': 'Classic'},
            {'label': 'Clear', 'value': 'Clear'},
            {'label': 'Col-Erase', 'value': 'Col-Erase'},
            {'label': 'Collection System', 'value': 'Collection System'},
            {'label': 'Coloredge', 'value': 'Coloredge'},
            {'label': 'Colorific', 'value': 'Colorific'},
            {'label': 'Commercial', 'value': 'Commercial'},
            {'label': 'Compact', 'value': 'Compact'},
            {'label': 'Companion', 'value': 'Companion'},
            {'label': 'Contico', 'value': 'Contico'},
            {'label': 'Crayola', 'value': 'Crayola'},
            {'label': 'Cubify', 'value': 'Cubify'},
            {'label': 'Cush', 'value': 'Cush'},
            {'label': 'Cyber', 'value': 'Cyber'},
            {'label': 'DAX', 'value': 'DAX'},
            {'label': 'DMI', 'value': 'DMI'},
            {'label': 'DXL', 'value': 'DXL'},
            {'label': 'DYMO', 'value': 'DYMO'},
            {'label': 'Dana', 'value': 'Dana'},
            {'label': 'Data Products', 'value': 'Data Products'},
            {'label': 'Decoflex', 'value': 'Decoflex'},
            {'label': 'Deflect', 'value': 'Deflect'},
            {'label': 'Dell', 'value': 'Dell'},
            {'label': 'Deluxe', 'value': 'Deluxe'},
            {'label': 'Design', 'value': 'Design'},
            {'label': 'Design Rectangular and Half-Moon Meeting Room Tables', 'value': 'Design Rectangular and Half-Moon Meeting Room Tables'},
            {'label': 'Dexim', 'value': 'Dexim'},
            {'label': 'Digium', 'value': 'Digium'},
            {'label': 'Disposable', 'value': 'Disposable'},
            {'label': 'Dixon', 'value': 'Dixon'},
            {'label': 'Dot', 'value': 'Dot'},
            {'label': 'Dual', 'value': 'Dual'},
            {'label': 'Durable', 'value': 'Durable'},
            {'label': 'Easy', 'value': 'Easy'},
            {'label': 'Eaton', 'value': 'Eaton'},
            {'label': 'Eberhard', 'value': 'Eberhard'},
            {'label': 'Eco Tones', 'value': 'Eco Tones'},
            {'label': 'Eldon', 'value': 'Eldon'},
            {'label': 'Eletrix', 'value': 'Eletrix'},
            {'label': 'Elite', 'value': 'Elite'},
            {'label': 'Embossed', 'value': 'Embossed'},
            {'label': 'Enermax', 'value': 'Enermax'},
            {'label': 'Epson', 'value': 'Epson'},
            {'label': 'Eureka', 'value': 'Eureka'},
            {'label': 'Euro-Pro', 'value': 'Euro-Pro'},
            {'label': 'Executive', 'value': 'Executive'},
            {'label': 'Faber', 'value': 'Faber'},
            {'label': 'Fashion', 'value': 'Fashion'},
            {'label': 'Fellowes', 'value': 'Fellowes'},
            {'label': 'File', 'value': 'File'},
            {'label': 'First Data', 'value': 'First Data'},
            {'label': 'Fiskars', 'value': 'Fiskars'},
            {'label': 'Flexible', 'value': 'Flexible'},
            {'label': 'Floodlight', 'value': 'Floodlight'},
            {'label': 'G.E.', 'value': 'G.E.'},
            {'label': 'GBC', 'value': 'GBC'},
            {'label': 'Ge', 'value': 'Ge'},
            {'label': 'Gear', 'value': 'Gear'},
            {'label': 'Geemarc', 'value': 'Geemarc'},
            {'label': 'Geographics', 'value': 'Geographics'},
            {'label': 'Global', 'value': 'Global'},
            {'label': 'Globe', 'value': 'Globe'},
            {'label': 'Google', 'value': 'Google'},
            {'label': 'Gould', 'value': 'Gould'},
            {'label': 'Grandstream', 'value': 'Grandstream'},
            {'label': 'Great White', 'value': 'Great White'},
            {'label': 'Green', 'value': 'Green'},
            {'label': 'Griffin', 'value': 'Griffin'},
            {'label': 'HP', 'value': 'HP'},
            {'label': 'HTC', 'value': 'HTC'},
            {'label': 'Hammermill', 'value': 'Hammermill'},
            {'label': 'Harbour', 'value': 'Harbour'},
            {'label': 'Harmony', 'value': 'Harmony'},
            {'label': 'Heavy-Duty', 'value': 'Heavy-Duty'},
            {'label': 'Hewlett-Packard', 'value': 'Hewlett-Packard'},
            {'label': 'Holmes', 'value': 'Holmes'},
            {'label': 'Home/Office', 'value': 'Home/Office'},
            {'label': 'Homely Harmony', 'value': 'Homely Harmony'},
            {'label': 'Hon', 'value': 'Hon'},
            {'label': 'Honey Well', 'value': 'Honey Well'},
            {'label': 'Hoover', 'value': 'Hoover'},
            {'label': 'Howard Miller', 'value': 'Howard Miller'},
            {'label': 'Hunt', 'value': 'Hunt'},
            {'label': 'Hypercom', 'value': 'Hypercom'},
            {'label': 'I.R.I.S', 'value': 'I.R.I.S'},
            {'label': 'IBM', 'value': 'IBM'},
            {'label': 'Ibico', 'value': 'Ibico'},
            {'label': 'Iceberg', 'value': 'Iceberg'},
            {'label': 'Ideal', 'value': 'Ideal'},
            {'label': 'Ikross', 'value': 'Ikross'},
            {'label': 'Imation', 'value': 'Imation'},
            {'label': 'Important', 'value': 'Important'},
            {'label': 'Ink', 'value': 'Ink'},
            {'label': 'Innergie', 'value': 'Innergie'},
            {'label': 'Insertable', 'value': 'Insertable'},
            {'label': 'Inter-Office', 'value': 'Inter-Office'},
            {'label': 'Iris', 'value': 'Iris'},
            {'label': 'JBL', 'value': 'JBL'},
            {'label': 'JM', 'value': 'JM'},
            {'label': 'Jabra', 'value': 'Jabra'},
            {'label': 'Jackery', 'value': 'Jackery'},
            {'label': 'Jawbone', 'value': 'Jawbone'},
            {'label': 'Jensen', 'value': 'Jensen'},
            {'label': 'Jet-Pak', 'value': 'Jet-Pak'},
            {'label': 'Jiffy', 'value': 'Jiffy'},
            {'label': 'KI', 'value': 'KI'},
            {'label': 'Kensington', 'value': 'Kensington'},
            {'label': 'Key Tronic', 'value': 'Key Tronic'},
            {'label': 'Kingston', 'value': 'Kingston'},
            {'label': 'Konftel', 'value': 'Konftel'},
            {'label': 'Konica Minolta', 'value': 'Konica Minolta'},
            {'label': 'LF', 'value': 'LF'},
            {'label': 'LG', 'value': 'LG'},
            {'label': 'Laminate', 'value': 'Laminate'},
            {'label': 'Lenovo', 'value': 'Lenovo'},
            {'label': 'Lesro', 'value': 'Lesro'},
            {'label': 'Lexmark', 'value': 'Lexmark'},
            {'label': 'Lifetime', 'value': 'Lifetime'},
            {'label': 'Linden', 'value': 'Linden'},
            {'label': 'Lock-Up', 'value': 'Lock-Up'},
            {'label': 'Logitech', 'value': 'Logitech'},
            {'label': 'Longer-Life', 'value': 'Longer-Life'},
            {'label': 'Loose', 'value': 'Loose'},
            {'label': 'Lunatik', 'value': 'Lunatik'},
            {'label': 'Luxo', 'value': 'Luxo'},
            {'label': 'Macally', 'value': 'Macally'},
            {'label': 'Magna', 'value': 'Magna'},
            {'label': 'Magnifier', 'value': 'Magnifier'},
            {'label': 'Manco', 'value': 'Manco'},
            {'label': 'Manila', 'value': 'Manila'},
            {'label': 'Martin-Yale', 'value': 'Martin-Yale'},
            {'label': 'Master', 'value': 'Master'},
            {'label': 'Maxell', 'value': 'Maxell'},
            {'label': 'Mead', 'value': 'Mead'},
            {'label': 'Mediabridge', 'value': 'Mediabridge'},
            {'label': 'Memo', 'value': 'Memo'},
            {'label': 'Memorex', 'value': 'Memorex'},
            {'label': 'Micro', 'value': 'Micro'},
            {'label': 'Micro Spectra', 'value': 'Micro Spectra'},
            {'label': 'Microsoft', 'value': 'Microsoft'},
            {'label': 'Mitel', 'value': 'Mitel'},
            {'label': 'Mophie', 'value': 'Mophie'},
            {'label': 'Motorola', 'value': 'Motorola'},
            {'label': 'Multi', 'value': 'Multi'},
            {'label': 'NETGEAR', 'value': 'NETGEAR'},
            {'label': 'Neat', 'value': 'Neat'},
            {'label': 'Newell', 'value': 'Newell'},
            {'label': 'Nexus Nova', 'value': 'Nexus Nova'},
            {'label': 'Nokia', 'value': 'Nokia'},
            {'label': 'Nortel', 'value': 'Nortel'},
            {'label': 'Novimex', 'value': 'Novimex'},
            {'label': 'Nu-Dell', 'value': 'Nu-Dell'},
            {'label': "O'Sullivan", 'value': "O'Sullivan"},
            {'label': 'OIC', 'value': 'OIC'},
            {'label': 'Office Impressions', 'value': 'Office Impressions'},
            {'label': 'Office Orbit', 'value': 'Office Orbit'},
            {'label': 'Office Star', 'value': 'Office Star'},
            {'label': 'Okidata', 'value': 'Okidata'},
            {'label': 'Ooma', 'value': 'Ooma'},
            {'label': 'Otter Box', 'value': 'Otter Box'},
            {'label': 'PNY', 'value': 'PNY'},
            {'label': 'Panasonic', 'value': 'Panasonic'},
            {'label': 'Park', 'value': 'Park'},
            {'label': 'Pay Anywhere', 'value': 'Pay Anywhere'},
            {'label': 'Pearl', 'value': 'Pearl'},
            {'label': 'Peel', 'value': 'Peel'},
            {'label': 'Peel & Seel', 'value': 'Peel & Seel'},
            {'label': 'Peel & Stick', 'value': 'Peel & Stick'},
            {'label': 'Pen Power', 'value': 'Pen Power'},
            {'label': 'Perixx', 'value': 'Perixx'},
            {'label': 'Perma', 'value': 'Perma'},
            {'label': 'Petty', 'value': 'Petty'},
            {'label': 'Pizaaz', 'value': 'Pizaaz'},
            {'label': 'Plantronics', 'value': 'Plantronics'},
            {'label': 'Plymouth', 'value': 'Plymouth'},
            {'label': 'Pocket Pro', 'value': 'Pocket Pro'},
            {'label': 'Poly', 'value': 'Poly'},
            {'label': 'Power Gen', 'value': 'Power Gen'},
            {'label': 'Prang', 'value': 'Prang'},
            {'label': 'Premier', 'value': 'Premier'},
            {'label': 'Presstex', 'value': 'Presstex'},
            {'label': 'Prestige', 'value': 'Prestige'},
            {'label': 'Prisma', 'value': 'Prisma'},
            {'label': 'Project', 'value': 'Project'},
            {'label': 'Pure Gear', 'value': 'Pure Gear'},
            {'label': 'Pyle', 'value': 'Pyle'},
            {'label': 'QVS', 'value': 'QVS'},
            {'label': 'Quartet', 'value': 'Quartet'},
            {'label': 'RCA', 'value': 'RCA'},
            {'label': 'RSVP', 'value': 'RSVP'},
            {'label': 'Razer', 'value': 'Razer'},
            {'label': 'Recycled', 'value': 'Recycled'},
            {'label': 'Redi-Strip', 'value': 'Redi-Strip'},
            {'label': 'Rediform', 'value': 'Rediform'},
            {'label': 'Regeneration', 'value': 'Regeneration'},
            {'label': 'Revere', 'value': 'Revere'},
            {'label': 'Ricoh', 'value': 'Ricoh'},
            {'label': 'Riverleaf', 'value': 'Riverleaf'},
            {'label': 'Riverside', 'value': 'Riverside'},
            {'label': 'Rogers', 'value': 'Rogers'},
            {'label': 'Rosewill', 'value': 'Rosewill'},
            {'label': 'Round', 'value': 'Round'},
            {'label': 'Rubber', 'value': 'Rubber'},
            {'label': 'Rush', 'value': 'Rush'},
            {'label': 'Sabrent', 'value': 'Sabrent'},
            {'label': 'Safco', 'value': 'Safco'},
            {'label': 'Samsung', 'value': 'Samsung'},
            {'label': 'San Disk', 'value': 'San Disk'},
            {'label': 'Sanford', 'value': 'Sanford'},
            {'label': 'Sanitaire', 'value': 'Sanitaire'},
            {'label': 'Sannysis', 'value': 'Sannysis'},
            {'label': 'Sanyo', 'value': 'Sanyo'},
            {'label': 'Satellite', 'value': 'Satellite'},
            {'label': 'Sauder', 'value': 'Sauder'},
            {'label': 'Seidio', 'value': 'Seidio'},
            {'label': 'Seth Thomas', 'value': 'Seth Thomas'},
            {'label': 'Sharp', 'value': 'Sharp'},
            {'label': 'ShoreTel', 'value': 'ShoreTel'},
            {'label': 'SimpliFile', 'value': 'SimpliFile'},
            {'label': 'Situations', 'value': 'Situations'},
            {'label': 'Skilcraft', 'value': 'Skilcraft'},
            {'label': 'Slim View', 'value': 'Slim View'},
            {'label': 'Smart', 'value': 'Smart'},
            {'label': 'Smead', 'value': 'Smead'},
            {'label': 'Snap-A-Way', 'value': 'Snap-A-Way'},
            {'label': 'Socket', 'value': 'Socket'},
            {'label': 'Sony', 'value': 'Sony'},
            {'label': 'Sortfiler', 'value': 'Sortfiler'},
            {'label': 'Southworth', 'value': 'Southworth'},
            {'label': 'Space', 'value': 'Space'},
            {'label': 'Speck', 'value': 'Speck'},
            {'label': 'Spectrum Snippets', 'value': 'Spectrum Snippets'},
            {'label': 'Speediset', 'value': 'Speediset'},
            {'label': 'Spigen', 'value': 'Spigen'},
            {'label': 'Spiral Bound', 'value': 'Spiral Bound'},
            {'label': 'Square', 'value': 'Square'},
            {'label': 'Stanley', 'value': 'Stanley'},
            {'label': 'Star Tech', 'value': 'Star Tech'},
            {'label': 'Steel', 'value': 'Steel'},
            {'label': 'Sterilite', 'value': 'Sterilite'},
            {'label': 'Sterling', 'value': 'Sterling'},
            {'label': 'Stiletto', 'value': 'Stiletto'},
            {'label': 'Stockwell', 'value': 'Stockwell'},
            {'label': 'Storex', 'value': 'Storex'},
            {'label': 'Strathmore', 'value': 'Strathmore'},
            {'label': 'Stride', 'value': 'Stride'},
            {'label': 'Super', 'value': 'Super'},
            {'label': 'Surelock', 'value': 'Surelock'},
            {'label': 'Swingline', 'value': 'Swingline'},
            {'label': 'TRENDnet', 'value': 'TRENDnet'},
            {'label': 'TUF', 'value': 'TUF'},
            {'label': 'Telescoping', 'value': 'Telescoping'},
            {'label': 'Tenex', 'value': 'Tenex'},
            {'label': 'Tennsco', 'value': 'Tennsco'},
            {'label': 'Tennsco ', 'value': 'Tennsco '},
            {'label': 'Tensor', 'value': 'Tensor'},
            {'label': 'Texas Instruments', 'value': 'Texas Instruments'},
            {'label': 'Tops', 'value': 'Tops'},
            {'label': 'Toshiba', 'value': 'Toshiba'},
            {'label': 'Trav', 'value': 'Trav'},
            {'label': 'Trimflex', 'value': 'Trimflex'},
            {'label': 'Tripp', 'value': 'Tripp'},
            {'label': 'Tuff', 'value': 'Tuff'},
            {'label': 'Tyvek', 'value': 'Tyvek'},
            {'label': 'Ultra', 'value': 'Ultra'},
            {'label': 'UniKeep', 'value': 'UniKeep'},
            {'label': 'Universal', 'value': 'Universal'},
            {'label': 'V7', 'value': 'V7'},
            {'label': 'VTech', 'value': 'VTech'},
            {'label': 'Vari Cap6', 'value': 'Vari Cap6'},
            {'label': 'Verbatim', 'value': 'Verbatim'},
            {'label': 'Vinyl', 'value': 'Vinyl'},
            {'label': 'Vtech', 'value': 'Vtech'},
            {'label': 'WD', 'value': 'WD'},
            {'label': 'Wasp', 'value': 'Wasp'},
            {'label': 'Wausau', 'value': 'Wausau'},
            {'label': 'Westing House', 'value': 'Westing House'},
            {'label': 'Weyer Haeuser', 'value': 'Weyer Haeuser'},
            {'label': 'White', 'value': 'White'},
            {'label': 'Wi-Ex', 'value': 'Wi-Ex'},
            {'label': 'Wilson', 'value': 'Wilson'},
            {'label': 'Wilson Jones', 'value': 'Wilson Jones'},
            {'label': 'Wire Bound', 'value': 'Wire Bound'},
            {'label': 'WireTech', 'value': 'WireTech'},
            {'label': 'Wireless', 'value': 'Wireless'},
            {'label': 'X-Rack', 'value': 'X-Rack'},
            {'label': 'Xblue', 'value': 'Xblue'},
            {'label': 'Xerox', 'value': 'Xerox'},
            {'label': 'Xiaomi', 'value': 'Xiaomi'},
            {'label': 'XtraLife', 'value': 'XtraLife'},
            {'label': 'ZAGG', 'value': 'ZAGG'},
            {'label': 'Zebra', 'value': 'Zebra'},
            {'label': 'Zipper', 'value': 'Zipper'},
            {'label': 'i.Sound', 'value': 'i.Sound'},
            {'label': 'iHome', 'value': 'iHome'},
            {'label': 'iOttie', 'value': 'iOttie'},
            {'label': 'netTALK', 'value': 'netTALK'}
        ],
        value='APC',
        placeholder="All Brands are Included",
        style={'width': '20rem', 'color': 'black', 'text-align': 'center'}
    ))
])  

side_1 = html.Div([
    html.Center(
        children=html.Div([
            html.H3('Year Filter:')
        ], style = {'padding-bottom': '5px', 'width': '90%', "padding-top": "5px"})
    ),
    html.Center(dcc.Dropdown(
        id='year_option',
        options=[
            {'label': '2010', 'value': 2010},
            {'label': '2011', 'value': 2011},
            {'label': '2012', 'value': 2012},
            {'label': '2013', 'value': 2013},
            {'label': '2014', 'value': 2014},
            {'label': '2015', 'value': 2015},
        ],
        value=2010,
        clearable=False,
        style={'width': '20rem', 'color': 'black', 'text-align': 'center'}
    ))
])

side_2 = html.Div([
    html.Center(
        children=html.Div([
            html.H3('Is Discounted Filter:')
        ], style = {'padding-bottom': '5px', 'width': '90%', "padding-top": "5px"})
    ),
    html.Center(dcc.Dropdown(
        id='is_discounted_option',
        options=[
            {'label': 'Discounted', 'value': 1},
            {'label': 'Not Discounted', 'value': 0},
        ],
        value=1,
        placeholder="Ignore Filter",
        style={'width': '20rem', 'color': 'black', 'text-align': 'center'}
    ))
])

# Total Order Quantity Over Time
@app.callback(
    Output("output0", "children"), 
    Input('brand_name_option', 'value'),
    Input('year_option', 'value'),
    Input('is_discounted_option', 'value'))
def display_graph0(brand_name_option, year_option, is_discounted_option):

    # df_1 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/1_Superstore_Datamart_2015_Modified_v2.csv')
    # df_2 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/2_Superstore_Datamart_2015_Modified_v2.csv')
    # df_3 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/3_Superstore_Datamart_2015_Modified_v2.csv')

    # full_df = pd.concat([df_1,df_2,df_3])
    # df = full_df

    if  (brand_name_option is not None) and (is_discounted_option is not None):

        filtered_df = df[(df['ORDER_YEAR'] == year_option) & (df['BRAND_NAME'] == brand_name_option) & (df['IS_DISCOUNTED'] == is_discounted_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = filtered_df['BRAND_NAME'].iloc[0]

        if (is_discounted_option == 0):
            is_discount_value = 'Non-Discounted'
        else:
            is_discount_value = 'Discounted'

        title=f'Total Order Quantity Over Time - Year: {year_value}, Brand: {brand_name_value} ({is_discount_value})'

    elif  (brand_name_option is None) and (is_discounted_option is not None):

        filtered_df = df[(df['ORDER_YEAR'] == year_option) & (df['IS_DISCOUNTED'] == is_discounted_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = 'ALL Brands'

        if (is_discounted_option == 0):
            is_discount_value = 'Non-Discounted'
        else:
            is_discount_value = 'Discounted'

        title=f'Total Order Quantity Over Time - Year: {year_value}, Brand: {brand_name_value} ({is_discount_value})'

    elif  (brand_name_option is not None) and (is_discounted_option is None):

        filtered_df = df[(df['ORDER_YEAR'] == year_option) & (df['BRAND_NAME'] == brand_name_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = filtered_df['BRAND_NAME'].iloc[0]

        title=f'Total Order Quantity Over Time - Year: {year_value}, Brand: {brand_name_value}'

    elif (brand_name_option is None) and (is_discounted_option is None):

        #
        filtered_df = df[(df['ORDER_YEAR'] == year_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = 'ALL Brands'

        # 
        title=f'Total Order Quantity Over Time - Year: {year_value}, Brand: {brand_name_value}'
    
    # Define the order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Group by 'ORDER_MONTH_NAME' and sum the 'QUANTITY'
    grouped_df = filtered_df.groupby('ORDER_MONTH_NAME')['QUANTITY'].sum().reset_index()

    # Convert 'ORDER_MONTH_NAME' to categorical with the defined order
    grouped_df['ORDER_MONTH_NAME'] = pd.Categorical(grouped_df['ORDER_MONTH_NAME'], categories=month_order, ordered=True)

    # Sort the DataFrame based on the categorical order
    grouped_df = grouped_df.sort_values('ORDER_MONTH_NAME')

    # Create a Line chart using Plotly
    fig = px.line(grouped_df, x='ORDER_MONTH_NAME', y='QUANTITY',
                title=title,
                labels={'ORDER_MONTH_NAME': 'Month', 'QUANTITY': 'Total Order Quantity'},
                height=1000, width=900,
                line_shape='linear', render_mode='auto'
                )

    # Add dots on each line for each month
    fig.update_traces(mode='markers+lines', marker=dict(size=10))

    # Customize layout
    fig.update_layout(
        font=dict(family='Roboto', size=14, color='white'),
        plot_bgcolor='#222222',
        paper_bgcolor='#222222',
        template="plotly_dark",
        title_x=0.5,
        xaxis_tickangle=-35,
        hoverlabel=dict(font=dict(family='Roboto', size=16, color='Black')),
    )

    # Update traces to customize hover template
    fig.update_traces(
        hovertemplate=f"<br>".join([
            # f"Year: {year_value}",
            # f"Brand: {brand_name_value}",
            "Month: <b>%{x}</b>",
            "<b><span style='text-decoration: underline; color: red;'>Total Quantity Ordered per Month:</span> %{y:,.0f}</b>",
        ]),
    )

    # Set the font color to black for the total transaction amount
    fig.update_traces(marker=dict(color='White'))

    return dbc.Col(dcc.Graph(figure=fig))

# Total Gross Profit Over Time
@app.callback(
    Output("output1", "children"), 
    Input('brand_name_option', 'value'),
    Input('year_option', 'value'),
    Input('is_discounted_option', 'value'))
def display_graph1(brand_name_option, year_option, is_discounted_option):

    # df_1 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/1_Superstore_Datamart_2015_Modified_v2.csv')
    # df_2 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/2_Superstore_Datamart_2015_Modified_v2.csv')
    # df_3 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/3_Superstore_Datamart_2015_Modified_v2.csv')

    # full_df = pd.concat([df_1,df_2,df_3])
    # df = full_df

    if  (brand_name_option is not None) and (is_discounted_option is not None):

        filtered_df = df[(df['ORDER_YEAR'] == year_option) & (df['BRAND_NAME'] == brand_name_option) & (df['IS_DISCOUNTED'] == is_discounted_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = filtered_df['BRAND_NAME'].iloc[0]

        if (is_discounted_option == 0):
            is_discount_value = 'Non-Discounted'
        else:
            is_discount_value = 'Discounted'

        title=f'Total Gross Profit Over Time - Year: {year_value}, Brand: {brand_name_value} ({is_discount_value})'

    elif  (brand_name_option is None) and (is_discounted_option is not None):

        filtered_df = df[(df['ORDER_YEAR'] == year_option) & (df['IS_DISCOUNTED'] == is_discounted_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = 'ALL Brands'

        if (is_discounted_option == 0):
            is_discount_value = 'Non-Discounted'
        else:
            is_discount_value = 'Discounted'

        title=f'Total Gross Profit Over Time - Year: {year_value}, Brand: {brand_name_value} ({is_discount_value})'

    elif  (brand_name_option is not None) and (is_discounted_option is None):

        filtered_df = df[(df['ORDER_YEAR'] == year_option) & (df['BRAND_NAME'] == brand_name_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = filtered_df['BRAND_NAME'].iloc[0]

        title=f'Total Gross Profit Over Time - Year: {year_value}, Brand: {brand_name_value}'

    elif (brand_name_option is None) and (is_discounted_option is None):

        #
        filtered_df = df[(df['ORDER_YEAR'] == year_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = 'ALL Brands'

        # 
        title=f'Total Gross Profit Over Time - Year: {year_value}, Brand: {brand_name_value}'

    # Define the order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Group by 'ORDER_MONTH_NAME' and sum the 'GROSS_PROFIT_DISCOUNTED_UNIT_AMOUNT'
    grouped_df = filtered_df.groupby('ORDER_MONTH_NAME')['GROSS_PROFIT_DISCOUNTED_UNIT_AMOUNT'].sum().reset_index()

    # Convert 'ORDER_MONTH_NAME' to categorical with the defined order
    grouped_df['ORDER_MONTH_NAME'] = pd.Categorical(grouped_df['ORDER_MONTH_NAME'], categories=month_order, ordered=True)

    # Sort the DataFrame based on the categorical order
    grouped_df = grouped_df.sort_values('ORDER_MONTH_NAME')

    # Create a Line chart using Plotly
    fig = px.line(grouped_df, x='ORDER_MONTH_NAME', y='GROSS_PROFIT_DISCOUNTED_UNIT_AMOUNT',
                title=title,
                labels={'ORDER_MONTH_NAME': 'Month', 'GROSS_PROFIT_DISCOUNTED_UNIT_AMOUNT': 'Total Gross Profit'},
                height=1000, width=900,
                line_shape='linear', render_mode='auto'
                )

    # Add dots on each line for each month
    fig.update_traces(mode='markers+lines', marker=dict(size=10))

    # Customize layout
    fig.update_layout(
        font=dict(family='Roboto', size=14, color='white'),
        plot_bgcolor='#222222',
        paper_bgcolor='#222222',
        template="plotly_dark",
        title_x=0.5,
        xaxis_tickangle=-35,
        hoverlabel=dict(font=dict(family='Roboto', size=16, color='Black')),
    )

    # Update traces to customize hover template
    fig.update_traces(
        hovertemplate=f"<br>".join([
            # f"Year: {year_value}",
            # f"Brand: {brand_name_value}",
            "Month: <b>%{x}</b>",
            "<b><span style='text-decoration: underline; color: red;'>Total Gross Profit per Month:</span> $%{y:,.0f}</b>",
        ]),
    )

    # Set the font color to black for the total transaction amount
    fig.update_traces(marker=dict(color='White'))

    return (dcc.Graph(figure=fig))

# Total Order Volume Over Time
@app.callback(
    Output("output2", "children"), 
    Input('brand_name_option', 'value'),
    Input('year_option', 'value'),
    Input('is_discounted_option', 'value'))
def display_graph2(brand_name_option, year_option, is_discounted_option):

    # df_1 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/1_Superstore_Datamart_2015_Modified_v2.csv')
    # df_2 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/2_Superstore_Datamart_2015_Modified_v2.csv')
    # df_3 = pd.read_csv('CSV_Datasets/4_Superstore_Modified_v2/3_Superstore_Datamart_2015_Modified_v2.csv')

    # full_df = pd.concat([df_1,df_2,df_3])
    # df = full_df

    if  (brand_name_option is not None) and (is_discounted_option is not None):

        filtered_df = df[(df['ORDER_YEAR'] == year_option) & (df['BRAND_NAME'] == brand_name_option) & (df['IS_DISCOUNTED'] == is_discounted_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = filtered_df['BRAND_NAME'].iloc[0]

        if (is_discounted_option == 0):
            is_discount_value = 'Non-Discounted'
        else:
            is_discount_value = 'Discounted'

        title=f'Total Volume of Orders Over Time - Year: {year_value}, Brand: {brand_name_value} ({is_discount_value})'

    elif  (brand_name_option is None) and (is_discounted_option is not None):

        filtered_df = df[(df['ORDER_YEAR'] == year_option) & (df['IS_DISCOUNTED'] == is_discounted_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = 'All Brands'

        if (is_discounted_option == 0):
            is_discount_value = 'Non-Discounted'
        else:
            is_discount_value = 'Discounted'

        title=f'Total Volume of Orders Over Time - Year: {year_value}, Brand: {brand_name_value} ({is_discount_value})'

    elif  (brand_name_option is not None) and (is_discounted_option is None):

        filtered_df = df[(df['ORDER_YEAR'] == year_option) & (df['BRAND_NAME'] == brand_name_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = filtered_df['BRAND_NAME'].iloc[0]

        title=f'Total Volume of Orders Over Time - Year: {year_value}, Brand: {brand_name_value}'

    elif (brand_name_option is None) and (is_discounted_option is None):

        #
        filtered_df = df[(df['ORDER_YEAR'] == year_option)]

        # Extract dynamic Year and Brand_name
        year_value = filtered_df['ORDER_YEAR'].iloc[0]
        brand_name_value = 'All Brands'

        # 
        title=f'Total Volume of Orders Over Time - Year: {year_value}, Brand: {brand_name_value}'

    # Define the order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Group by 'ORDER_MONTH_NAME' and get the count of orders
    grouped_df = filtered_df.groupby('ORDER_MONTH_NAME')['ORDER_DATE'].count().reset_index()

    # Convert 'ORDER_MONTH_NAME' to categorical with the defined order
    grouped_df['ORDER_MONTH_NAME'] = pd.Categorical(grouped_df['ORDER_MONTH_NAME'], categories=month_order, ordered=True)

    # Sort the DataFrame based on the categorical order
    grouped_df = grouped_df.sort_values('ORDER_MONTH_NAME')

    # Create a Line chart using Plotly
    fig = px.line(grouped_df, x='ORDER_MONTH_NAME', y='ORDER_DATE',
                title=title,
                labels={'ORDER_MONTH_NAME': 'Month', 'ORDER_DATE': 'Volume of Orders'},
                height=1000, width=900,
                line_shape='linear', render_mode='auto'
                )

    # Add dots on each line for each month
    fig.update_traces(mode='markers+lines', marker=dict(size=10))

    # Customize layout
    fig.update_layout(
        font=dict(family='Roboto', size=14, color='white'),
        plot_bgcolor='#222222',
        paper_bgcolor='#222222',
        template="plotly_dark",
        title_x=0.5,
        xaxis_tickangle=-35,
        hoverlabel=dict(font=dict(family='Roboto', size=16, color='Black')),
    )

    # Update traces to customize hover template
    fig.update_traces(
        hovertemplate=f"<br>".join([
            # f"Year: {year_value}",
            # f"Brand: {brand_name_value}",
            "Month: <b>%{x}</b>",
            "<b><span style='text-decoration: underline; color: red;'>Volume of Orders per Month:</span> %{y:,.0f}</b>",
        ]),
    )

    # Set the font color to black for the total transaction amount
    fig.update_traces(marker=dict(color='White'))

    return dbc.Col(dcc.Graph(figure=fig))

# APP LAYOUT
rows = html.Div(
    [dbc.Row([dbc.Col([side]),
              dbc.Col([side_1]),
              dbc.Col([side_2])], justify="center",),
     dbc.Row([dbc.Col(html.Div(id = 'output0'),width=5),
              dbc.Col(html.Div(id = 'output1'),width=5)], justify="evenly",),
     dbc.Row([dbc.Col(html.Div(id = 'output2'), width=5)], justify="center",), 
    ]
)

app.layout = html.Div([header, rows])

app.run_server(debug=False, port = 8050)