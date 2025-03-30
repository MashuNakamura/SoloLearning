def ip_to_int(ip_address):  
   octets = ip_address.split('.')
   result = 0
   for octet in octets:
    result = (result << 8) + int(octet)
    return result

def ips_between(start, end):
   start_int = ip_to_int(start)
   end_int = ip_to_int(end)
   return end_int - start_int

start_ip = "10.0.0.0"
end_ip = "10.0.0.50"
jumlah_ip = ips_between(start_ip, end_ip)
print(f"Jumlah IP antara {start_ip} dan {end_ip}: {jumlah_ip}")