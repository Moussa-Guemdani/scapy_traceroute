# from scapy.all import *
# import socket
# from scapy.layers.inet import IP
# from scapy.layers.inet import ICMP
# import csv

# google_adr = socket.gethostbyname('google.com')
# facebook_adr = socket.gethostbyname('facebook.com')
# youtube_adr = socket.gethostbyname('youtube.com')

# routers_twords_google_com = []
# routers_twords_facebook_com = []
# routers_twords_youtube_com = []

# google_rtts = []
# facebook_rtts = []
# youtube_rtts = []

# # ttl = nbr of hops
# ttl = 1

# while True:
        
#     ICMP_packet_to_google = IP(dst=str(google_adr), ttl=ttl)/ICMP()
#     google_reply = sr1(ICMP_packet_to_google, timeout=2)

#     ICMP_packet_to_facebook = IP(dst=str(facebook_adr), ttl=ttl)/ICMP()
#     facebook_reply = sr1(ICMP_packet_to_facebook, timeout=2)

#     ICMP_packet_to_youtube = IP(dst=str(youtube_adr), ttl=ttl)/ICMP()
#     youtube_reply = sr1(ICMP_packet_to_youtube, timeout=2)/ICMP()


#     google_hops_info = []
#     facebook_hops_info = []
#     youtube_hops_info = []



#     if google_reply:
#         router_ip = google_reply.src
#         routers_twords_google_com.append(router_ip)
#         google_hops_info.append([ttl, router_ip, google_reply.time])
#         # print(f"Hop {ttl}: {google_reply.src}")# gets the ip address of the gouter that replies
#         # print("google trace := ", routers_twords_google_com)

#         if google_reply.src == google_adr:
#             print('reached google.com destination ')
#             break

#     # else:
#     #     print(f"Hop {ttl}: *")
        


#     if facebook_reply:
#         print(f"Hop {ttl}: {facebook_reply.src}")# gets the ip address of the gouter that replies
#         routers_twords_facebook_com.append(facebook_reply.src)
#         # print("facebook trace := ", routers_twords_facebook_com)

#         if facebook_reply.src == facebook_adr:
#             print('reached facebook.com destination ')
#             break

#     else:
#         print(f"Hop {ttl}: *")

   

    
#     if youtube_reply:
#         print(f"Hop {ttl}: {youtube_reply.src}")# gets the ip address of the gouter that replies
#         routers_twords_youtube_com.append(youtube_reply.src)
#         # print("youtube trace := ", routers_twords_youtube_com)

#         if youtube_reply.src == youtube_adr:
#             print('reached youtube destination ')
#             break

#     else:
#         print(f"Hop {ttl}: *")

#     ttl += 1


# with open('routers_towards_google.txt', 'w') as google_file:
#     google_file.write('\n'.join(routers_twords_google_com))
#     # google_file.write((str(google_rtts)))

# with open('routers_towards_facebook.txt', 'w') as facebook_file:
#     facebook_file.write('\n'.join(routers_twords_facebook_com))

# with open('routers_towards_youtube.txt', 'w') as youtube_file:
#     youtube_file.write('\n'.join(routers_twords_youtube_com))



# with open('traceroute_results.csv', 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)

#     csv_writer.writerow(['TraceRoute google:'])
#     csv_writer.writerow(['Hop', 'Router_IP', 'RTT'])

#     for hop_info in google_hops_info:
#         csv_writer.writerow([*hop_info])

#     csv_writer.writerow([])

#     csv_writer.writerow(['TraceRoute Facebook:'])
#     csv_writer.writerow(['Hop', 'Router_IP', 'RTT'])
#     for hop_info in facebook_hops_info:
#         csv_writer.writerow([*hop_info])

#     csv_writer.writerow([])

#     csv_writer.writerow(['TraceRoute YouTube:'])
#     csv_writer.writerow(['Hop', 'Router_IP', 'RTT'])
#     for hop_info in youtube_hops_info:
#         csv_writer.writerow([*hop_info])


# # with open('traceroute_results.csv', 'w', newline='') as csv_file:
# #     csv_writer = csv.writer(csv_file)

# #     csv_writer.writerow(['traceroute toards Google:'])
# #     csv_writer.writerow(['Hop', 'Router_IP', 'First prob RTT', 'First prob RTT', 'Second prob RTT'])
# #     # csv_writer.writerow(google_hop_info)
# #     for google_results in google_hops:
# #         csv_writer.writerow(google_results)

# #     csv_writer.writerow([])  
# #     csv_writer.writerow(['traceroute toards Facebook'])
# #     csv_writer.writerow(['Hop', 'Router_IP', 'First prob RTT', 'Second prob RTT', 'Third prob RTT'])
# #     for facebook_result in facebook_hops:
# #         csv_writer.writerow(facebook_result)

# #     csv_writer.writerow([])  
# #     csv_writer.writerow(['traceroute toards Youtube'])
# #     csv_writer.writerow(['Hop', 'Router_IP', 'First prob RTT', 'Second prob RTT', 'Third prob RTT'])
# #     for youtube_result in youtube_hops:
# #         csv_writer.writerow(youtube_result)
            
    
# # params
# # hop number, router ip address, first prob rtt, second prob rtt, third prob rtt


from scapy.all import *
import socket
from scapy.layers.inet import IP
from scapy.layers.inet import ICMP
import csv


google_adr = socket.gethostbyname('google.com')
facebook_adr = socket.gethostbyname('facebook.com')
youtube_adr = socket.gethostbyname('youtube.com')

routers_towards_google_com = []
routers_towards_facebook_com = []
routers_towards_youtube_com = []

google_hop_info = []
facebook_hop_info = []
youtube_hop_info = []

# ttl = number of hops
ttl = 1

while True:
    ICMP_packet_to_google = IP(dst=google_adr, ttl=ttl) / ICMP()
    google_reply = sr1(ICMP_packet_to_google, timeout=2)

    ICMP_packet_to_facebook = IP(dst=facebook_adr, ttl=ttl) / ICMP()
    facebook_reply = sr1(ICMP_packet_to_facebook, timeout=2)

    ICMP_packet_to_youtube = IP(dst=youtube_adr, ttl=ttl) / ICMP()
    youtube_reply = sr1(ICMP_packet_to_youtube, timeout=2)

    if google_reply:
        router_ip = google_reply.src
        routers_towards_google_com.append(router_ip)
        google_hop_info.append([ttl, router_ip, google_reply.time])

        if router_ip == google_adr:
            print('Reached google.com destination')
            break

    if facebook_reply:
        router_ip = facebook_reply.src
        routers_towards_facebook_com.append(router_ip)
        facebook_hop_info.append([ttl, router_ip, facebook_reply.time])

        if router_ip == facebook_adr:
            print('Reached facebook.com destination')
            break

    if youtube_reply:
        router_ip = youtube_reply.src
        routers_towards_youtube_com.append(router_ip)
        youtube_hop_info.append([ttl, router_ip, youtube_reply.time])

        if router_ip == youtube_adr:
            print('Reached youtube.com destination')
            break

    ttl += 1


# calculating the shotest path
google_hops = len(routers_towards_google_com)
facebook_hops = len(routers_towards_facebook_com)
youtube_hops = len(routers_towards_youtube_com)

shortest_path_destination = None
shortest_path_hops = float('inf')

if google_hops < shortest_path_hops:
    shortest_path_destination = 'Path to Google'
    shortest_path_hops = google_hops

if facebook_hops < shortest_path_hops:
    shortest_path_destination = 'Path to Facebook'
    shortest_path_hops = facebook_hops
elif facebook_hops == shortest_path_hops:
    shortest_path_destination = 'Paths to Facebook & Google are equal and the shortest'

if youtube_hops < shortest_path_hops:
    shortest_path_destination = 'Path to YouTube'
    shortest_path_hops = youtube_hops
elif youtube_hops == shortest_path_hops:
    shortest_path_hops = 'Paths to Facebook & Google are equal and the shortest'



with open('routers_towards_google.txt', 'w') as google_file:
    google_file.write('\n'.join(routers_towards_google_com))

with open('routers_towards_facebook.txt', 'w') as facebook_file:
    facebook_file.write('\n'.join(routers_towards_facebook_com))

with open('routers_towards_youtube.txt', 'w') as youtube_file:
    youtube_file.write('\n'.join(routers_towards_youtube_com))


with open('traceroute_results.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['Google_traceroute:'])
    csv_writer.writerow(['Destination', 'Hop', 'Router_IP', 'RTT'])
    for hop_info in google_hop_info:
        csv_writer.writerow(['Google.com', *hop_info])

    csv_writer.writerow([])

    csv_writer.writerow(['Facebook_traceroute:'])
    csv_writer.writerow(['Destination', 'Hop', 'Router_IP', 'RTT'])
    for hop_info in facebook_hop_info:
        csv_writer.writerow(['Facebook.com', *hop_info])

    csv_writer.writerow([])

    csv_writer.writerow(['Youtube_traceroute:'])
    csv_writer.writerow(['Destination', 'Hop', 'Router_IP', 'RTT'])
    for hop_info in youtube_hop_info:
        csv_writer.writerow(['YouTube.com', *hop_info])

    csv_writer.writerow([])
    csv_writer.writerow(['Shortest Path'])
    csv_writer.writerow(['Destination', 'Hops'])
    csv_writer.writerow([shortest_path_destination, shortest_path_hops])
    