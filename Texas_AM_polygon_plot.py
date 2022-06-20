import folium
import streamlit as st
from streamlit_folium import folium_static

st.sidebar.title("Display paths")
submitted = st.sidebar.button("Show Paths")
st.write("**Path Map**")

def add_line_to_map(path_map, pair_of_positions, start="green", end="blue"):
    # folium.Marker(location=pair_of_positions[0], icon=folium.Icon(color=start, icon='shopping-cart'),
    #               popup='start').add_to(
    #     path_map)
    # folium.Marker(location=pair_of_positions[1], icon=folium.Icon(color=end, icon='home'), popup='end').add_to(
    #     path_map)

    folium.PolyLine(locations=[pair_of_positions], color="green").add_to(path_map)
    # arrows = get_arrows(locations=pair_of_positions, color="black", n_arrows=3)
    # for arrow in arrows:
    #     arrow.add_to(path_map)



bound_coord_list = [[30.62288148207414, -96.32925373851037], [30.62294610903063, -96.32792438246062], [30.62301072100539, -96.32659505471207], [30.62157848077359, -96.32659505471207], [30.621643075995276, -96.32526575526667], [30.620210817791307, -96.32526575526667], [30.620275396261373, -96.32393648412632], [30.618843120087526, -96.32393648412632], [30.618907681807425, -96.32260724129291], [30.617475387665984, -96.32260724129291], [30.617410827717922, -96.3239364841263], [30.61597851915481, -96.3239364841263], [30.615913946001527, -96.32526575526667], [30.615849357870193, -96.32659505471207], [30.614417036661468, -96.32659505471207], [30.61435243532474, -96.32792438246062], [30.61292009970097, -96.32792438246062], [30.612855485159084, -96.32925373851037], [30.611423135123285, -96.32925373851037], [30.61135850737646, -96.3305831228594], [30.61129386464967, -96.33191253550578], [30.609861501980117, -96.33191253550578], [30.60979684604823, -96.33324197644764], [30.60836446897328, -96.33324197644764], [30.608299799836537, -96.33457144568298], [30.606867408359204, -96.33457144568298], [30.606802726017825, -96.33590094320995], [30.605370320141134, -96.33590094320995], [30.60530562459533, -96.33723046902658], [30.605240914067256, -96.33856002313097], [30.603808495572313, -96.33856002313097], [30.603743771839667, -96.3398896055212], [30.602311338952, -96.3398896055212], [30.600878889895338, -96.3398896055212], [30.60094361007043, -96.33856002313097], [30.59951114306798, -96.33856002313097], [30.599575846482637, -96.33723046902658], [30.598143361536657, -96.33723046902658], [30.59671086042804, -96.33723046902658], [30.596646160571186, -96.33856002313097], [30.59521364508133, -96.33856002313097], [30.595148932023516, -96.3398896055212], [30.593716402155433, -96.3398896055212], [30.593651675896886, -96.34121921619534], [30.59358693465704, -96.34254885515146], [30.59215439219456, -96.34254885515146], [30.59208963775383, -96.34387852238766], [30.59065708091977, -96.34387852238766], [30.59059231327839, -96.34520821790198], [30.589159742075772, -96.34520821790198], [30.589094961233965, -96.34653794169253], [30.587662375665808, -96.34653794169253], [30.587597581623804, -96.34786769375738], [30.586164981693134, -96.34786769375738], [30.58622977395194, -96.34653794169253], [30.584797156094588, -96.34653794169253], [30.58486193158805, -96.34520821790198], [30.584926692100353, -96.34387852238766], [30.583494054535883, -96.34387852238766], [30.5835587982855, -96.34254885515146], [30.58212614279918, -96.34254885515146], [30.582190869787574, -96.34121921619534], [30.580758196381677, -96.34121921619534], [30.58069347117553, -96.34254885515146], [30.579260783416817, -96.34254885515146], [30.579196045015205, -96.34387852238766], [30.577763342906692, -96.34387852238766], [30.57769859130984, -96.34520821790198], [30.576265874854535, -96.34520821790198], [30.57620111006268, -96.34653794169253], [30.574768379263613, -96.34653794169253], [30.574703601276983, -96.34786769375738], [30.57463880831053, -96.34919747409461], [30.573206064955997, -96.34919747409461], [30.57177330547848, -96.34919747409461], [30.571708501102965, -96.35052728270227], [30.5716436817469, -96.35185711957847], [30.570210909721165, -96.35185711957847], [30.57014607717063, -96.35318698472126], [30.570081229638372, -96.35451687812872], [30.56864844506906, -96.35451687812872], [30.568583584342196, -96.35584679979894], [30.56851870863245, -96.35717674973], [30.568453817939012, -96.35850672791993], [30.5670210226197, -96.35850672791993], [30.56695611873114, -96.35983673436685], [30.566891199857746, -96.36116676906883], [30.565458392005183, -96.36116676906883], [30.565393459936516, -96.36249683202392], [30.563960637764378, -96.36249683202392], [30.563895692500683, -96.36382692323023], [30.56383073225061, -96.3651570426858], [30.562397897553492, -96.3651570426858], [30.562332924108247, -96.36648719038872], [30.562267935675457, -96.36781736633706], [30.562202932254323, -96.3691475705289], [30.560770086829923, -96.3691475705289], [30.560705070213114, -96.3704778029623], [30.5606400386068, -96.37180806363536], [30.55920718066776, -96.37180806363536], [30.55914213586563, -96.37313835254612], [30.55907707607283, -96.37446866969266], [30.559012001288583, -96.37579901507307], [30.557579132635055, -96.37579901507307], [30.55751404465448, -96.37712938868542], [30.55744894168129, -96.37845979052776], [30.558881806742566, -96.37845979052776], [30.558816686979203, -96.37979022059818], [30.560249534145093, -96.37979022059818], [30.561682365210135, -96.37979022059818], [30.563115180172076, -96.37979022059818], [30.564547979028678, -96.37979022059818], [30.564613105977244, -96.37845979052776], [30.566045890522116, -96.37845979052776], [30.5661110042706, -96.37712938868542], [30.567543774500713, -96.37712938868542], [30.567608875048872, -96.37579901507307], [30.56767396060226, -96.37446866969266], [30.569106718308806, -96.37446866969266], [30.569171790662008, -96.37313835254612], [30.57060453404713, -96.37313835254612], [30.570539459900314, -96.37446866969266], [30.57047437075868, -96.37579901507307], [30.571907094439073, -96.37579901507307], [30.571841988507554, -96.37712938868542], [30.57327469427454, -96.37712938868542], [30.573209571551686, -96.37845979052776], [30.57464225940297, -96.37845979052776], [30.574577119887334, -96.37979022059818], [30.57600978982062, -96.37979022059818], [30.575944633510744, -96.38112067889475], [30.575879462200408, -96.38245116541555], [30.57731211241818, -96.38245116541555], [30.577246924310952, -96.38378168015862], [30.57867955660591, -96.38378168015862], [30.58011217277145, -96.38378168015862], [30.580177364469417, -96.38245116541555], [30.5816099662984, -96.38245116541555], [30.58167514478852, -96.38112067889475], [30.58310773227791, -96.38112067889475], [30.583172897559958, -96.37979022059818], [30.58323804784023, -96.37845979052776], [30.58467062278048, -96.37845979052776], [30.584735759852816, -96.37712938868542], [30.58616832044683, -96.37712938868542], [30.586103181581635, -96.37845979052776], [30.58753572424145, -96.37845979052776], [30.58747056858133, -96.37979022059818], [30.588903093304662, -96.37979022059818], [30.588837920848178, -96.38112067889475], [30.59027042763273, -96.38112067889475], [30.590335601882366, -96.37979022059818], [30.591768094312197, -96.37979022059818], [30.591833255350515, -96.37845979052776], [30.593265733422623, -96.37845979052776], [30.593330881249376, -96.37712938868542], [30.593396014073004, -96.37579901507307], [30.594828479575693, -96.37579901507307], [30.594893599187905, -96.37446866969266], [30.59632605032621, -96.37446866969266], [30.596391156726778, -96.37313835254612], [30.597823593497683, -96.37313835254612], [30.59925601410863, -96.37313835254612], [30.599321109086848, -96.37180806363536], [30.599386189063424, -96.3704778029623], [30.597953764873832, -96.3704778029623], [30.59801882806086, -96.3691475705289], [30.599451254039156, -96.3691475705289], [30.599516304014827, -96.36781736633706], [30.60094871561846, -96.36781736633706], [30.601013752382546, -96.36648719038872], [30.601078774147734, -96.3651570426858], [30.601143780914832, -96.36382692323023], [30.601208772684615, -96.36249683202392], [30.60264117527053, -96.36249683202392], [30.60257618171451, -96.36382692323023], [30.602511173160774, -96.3651570426858], [30.603943556006044, -96.3651570426858], [30.603878530666904, -96.36648719038872], [30.605310895555483, -96.36648719038872], [30.60524585342948, -96.36781736633706], [30.606678200359067, -96.36781736633706], [30.606613141444765, -96.3691475705289], [30.60518079630254, -96.3691475705289], [30.603748434988635, -96.3691475705289], [30.603683364647917, -96.3704778029623], [30.603618279305095, -96.37180806363536], [30.603553178959377, -96.37313835254612], [30.60498553490814, -96.37313835254612], [30.606417874685764, -96.37313835254612], [30.606352755758092, -96.37446866969266], [30.6077850775735, -96.37446866969266], [30.60771994185122, -96.37579901507307], [30.60915224570211, -96.37579901507307], [30.609087093183785, -96.37712938868542], [30.609021925657714, -96.37845979052776], [30.610454209752053, -96.37845979052776], [30.610389025427278, -96.37979022059818], [30.6118212915523, -96.37979022059818], [30.61175609042735, -96.38112067889475], [30.613188338580752, -96.38112067889475], [30.61312312065421, -96.38245116541555], [30.61455535083371, -96.38245116541555], [30.61462057055072, -96.38112067889475], [30.616052786335008, -96.38112067889475], [30.61611799283006, -96.37979022059818], [30.617550194216104, -96.37979022059818], [30.617615387488982, -96.37845979052776], [30.619047574473772, -96.37845979052776], [30.619112754524245, -96.37712938868542], [30.62054492710476, -96.37712938868542], [30.621977083490115, -96.37712938868542], [30.62340922367809, -96.37712938868542], [30.624841347666436, -96.37712938868542], [30.626273455452935, -96.37712938868542], [30.627705547035337, -96.37712938868542], [30.629137622411417, -96.37712938868542], [30.62920279996369, -96.37579901507307], [30.630634860917983, -96.37579901507307], [30.63070002524377, -96.37446866969266], [30.630765174557105, -96.37313835254612], [30.63219722287234, -96.37313835254612], [30.632262358959345, -96.37180806363536], [30.633694392846163, -96.37180806363536], [30.633759515706604, -96.3704778029623], [30.632327480035062, -96.37047780296231], [30.632392586100284, -96.3691475705289], [30.63096053243032, -96.3691475705289], [30.631025621701774, -96.36781736633706], [30.629593550035676, -96.36781736633706], [30.629658622514814, -96.36648719038872], [30.62972367998667, -96.3651570426858], [30.631155755220014, -96.3651570426858], [30.63122079946839, -96.36382692323023], [30.63128582871066, -96.36249683202392], [30.631350842947608, -96.36116676906883], [30.629918762366536, -96.36116676906883], [30.62998375981723, -96.35983673436685], [30.62855166124349, -96.35983673436685], [30.628616641909375, -96.35850672791993], [30.627184525345246, -96.35850672791993], [30.627249489227765, -96.35717674973], [30.62581735467555, -96.35717674973], [30.62438520391872, -96.35717674972999], [30.62445014923812, -96.35584679979894], [30.623017980497536, -96.35584679979894], [30.623082909036697, -96.35451687812872], [30.621650722314644, -96.35451687812872], [30.62171563407503, -96.35318698472126], [30.620283429373785, -96.35318698472126], [30.62034832435684, -96.35185711957847], [30.618916101678693, -96.35185711957847], [30.61898097988587, -96.35052728270227], [30.617548739233108, -96.35052728270227], [30.617613600665848, -96.34919747409461], [30.6176784471054, -96.34786769375738], [30.61774327855255, -96.34653794169253], [30.61917552454415, -96.34653794169253], [30.619240342778486, -96.34520821790198], [30.620672574353783, -96.34520821790198], [30.620737379375065, -96.34387852238766], [30.62216959653105, -96.34387852238766], [30.622104789731775, -96.34520821790198], [30.62353698891022, -96.34520821790198], [30.623472165340658, -96.34653794169253], [30.623407326777816, -96.34786769375738], [30.624839506197983, -96.34786769375738], [30.626271669414514, -96.34786769375738], [30.62770381642516, -96.34786769375738], [30.627638957532145, -96.34919747409461], [30.629071086556355, -96.34919747409461], [30.629006210888463, -96.35052728270227], [30.630438321923943, -96.35052728270227], [30.631870416747216, -96.35052728270227], [30.631935295972063, -96.34919747409461], [30.63200016019955, -96.34786769375738], [30.63056806181991, -96.34786769375738], [30.63063290927326, -96.34653794169253], [30.63069774173124, -96.34520821790198], [30.632129843665563, -96.34520821790198], [30.633561929384726, -96.34520821790198], [30.633626750401383, -96.34387852238766], [30.633691556423422, -96.34254885515146], [30.633756347451644, -96.34121921619534], [30.633821123486847, -96.3398896055212], [30.632389030664047, -96.3398896055212], [30.632453789932143, -96.33856002313097], [30.631021679118412, -96.33856002313097], [30.63108642162087, -96.33723046902658], [30.629654292818483, -96.33723046902658], [30.6282221478043, -96.33723046902658], [30.628286871767983, -96.33590094320995], [30.6283515807435, -96.33457144568298], [30.62841627473163, -96.33324197644764], [30.62698410818488, -96.33324197644764], [30.627048785412924, -96.33191253550578], [30.62561660088463, -96.33191253550578], [30.62568126135404, -96.3305831228594], [30.624249058846463, -96.3305831228594], [30.624313702558695, -96.32925373851037], [30.62288148207414, -96.32925373851037]]
if submitted:
    path_map = folium.Map(location=[30.62288148207414, -96.32925373851037], zoom_start=12, width="%100", height="%100")
    for i in range(len(bound_coord_list) - 1):
        add_line_to_map(path_map, [bound_coord_list[i], bound_coord_list[i + 1]])

    folium_static(path_map, width=700, height=500)