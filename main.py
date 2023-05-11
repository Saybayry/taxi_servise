from RouteCreate.mapRoute import create_route, calculate_price
import geocoder


def print_hi(name):
    import tkinter
    import tkintermapview

    # tkintermapview = address.convert_address_to_coordinates("Германа титова 17 Барнаул Алтайский край")
    address = tkintermapview.convert_address_to_coordinates("Германа титова 20 Барнаул Алтайский край")
    print(address)



    start_point = (83.788130, 53.345903)
    end_point = (83.723955, 53.382367)
    location = "Барнаул, Россия"
    arr_path,len = create_route(start_point,end_point,location)
    # print(arr)

    # create tkinter window
    root_tk = tkinter.Tk()
    root_tk.geometry(f"{800}x{600}")
    root_tk.title("map_view_example.py")


    # create map widget
    map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    # set current widget position and zoom
    map_widget.set_address(location)

    marker_1 = map_widget.set_position(start_point[1], start_point[0],marker=True)
    marker_1.set_text("начальная точка")
    marker_2 = map_widget.set_position(end_point[1], end_point[0], marker=True)
    marker_2.set_text("конечная точка")

    marker_3 = map_widget.set_position(address[0], address[1], marker=True)
    marker_3.set_text("каакая то")

    # marker_3 = map_widget.set_address("ул Титова 17 ,Барнаул, Россия", marker=True)
    # marker_3.set_text("конечная точка")



    path_1 = map_widget.set_path([marker_1.position, *arr_path, marker_2.position])
    print(calculate_price(len))


    root_tk.mainloop()
    pass



if __name__ == '__main__':
    print_hi('PyCharm')


# [(83.7879304, 53.3457072), (83.7876302, 53.3459793), (83.7853566, 53.3480355), (83.784176, 53.3491193), (83.7836292, 53.3496408), (83.7834895, 53.3497745), (83.7821693, 53.3509899), (83.7801144, 53.3528672), (83.7792196, 53.3536916), (83.778142, 53.3546825), (83.7780188, 53.3549164), (83.7784134, 53.3575074), (83.7784421, 53.3576957), (83.7755577, 53.357868), (83.770352, 53.3581815), (83.7706314, 53.3599756), (83.7708886, 53.3616248), (83.7709343, 53.3619365), (83.7705753, 53.3628065), (83.7703735, 53.3629497), (83.7665263, 53.3657381), (83.7662925, 53.3659449), (83.7659541, 53.366254), (83.7601531, 53.3713892), (83.7584809, 53.3728631), (83.7579607, 53.3732971), (83.7573183, 53.3738617), (83.7555527, 53.3754429), (83.7554041, 53.3755783), (83.7525173, 53.3744568), (83.7509742, 53.3738573), (83.7494851, 53.3732788), (83.7480953, 53.3745705), (83.7443577, 53.3780347), (83.7419412, 53.3802828), (83.7409704, 53.3811862), (83.7403627, 53.3817517), (83.7367544, 53.3851214), (83.7362852, 53.3851361), (83.7351429, 53.3850705), (83.7349357, 53.3849985), (83.7319417, 53.3838697), (83.729321, 53.3829319), (83.7280405, 53.382925), (83.7269783, 53.3825821), (83.7245703, 53.3825806)]
