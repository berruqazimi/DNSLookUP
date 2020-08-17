import dns.resolver
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('--value', help='value , REQUIRED', required=True)
args, unknown = parser.parse_known_args()
try:
    final = {}
    result = dns.resolver.resolve(args.value, 'A')
    try:
        result = dns.resolver.resolve(args.value, 'A')
        for ipval in result:
            final.update({'A': ipval.to_text()})
    except dns.resolver.NoAnswer:
        final.update({'A': 'No Record'})
    try:
        result = dns.resolver.resolve(args.value, 'AAAA')
        for ip6val in result:
            final.update({'AAAA': ip6val.to_text()})
    except dns.resolver.NoAnswer:
        final.update({'AAAA': 'No Record'})
    try:
        result = dns.resolver.resolve(args.value, 'CNAME')
        for cnameval in result:
            final.update({'CNAME': cnameval.to_text()})
    except dns.resolver.NoAnswer:
        final.update({'CNAME': 'No Record'})
    try:
        result = dns.resolver.resolve(args.value, 'MX')
        for mxeval in result:
            final.update({'MX': mxeval.to_text()})
    except dns.resolver.NoAnswer:
        final.update({'MX': 'No Record'})
    try:
        result = dns.resolver.resolve(args.value, 'NS')
        for nseval in result:
            final.update({'NS': nseval.to_text()})
    except dns.resolver.NoAnswer:
        final.update({'NS': 'No Record'})
    try:
        result = dns.resolver.resolve(args.value, 'PTR')
        for ptreval in result:
            final.update({'PTR': ptreval.to_text()})
    except dns.resolver.NoAnswer:
        final.update({'PTR': 'No Record'})
    try:
        result = dns.resolver.resolve(args.value, 'SRV')
        for svreval in result:
            final.update({'SRV': svreval.to_text()})
    except dns.resolver.NoAnswer:
        final.update({'SRV': 'No Record'})
    try:
        result = dns.resolver.resolve(args.value, 'SOA')
        for soaval in result:
            final.update({'SOA': soaval.to_text()})
    except dns.resolver.NoAnswer:
        final.update({'SOA': 'No Record'})
    try:
        result = dns.resolver.resolve(args.value, 'TXT')
        for txtval in result:
            final.update({'TXT': txtval.to_text()})
    except dns.resolver.NoAnswer:
        final.update({'TXT': 'No Record'})
    try:
        result = dns.resolver.resolve(args.value, 'CAA')
        for caaval in result:
            final.update({'CAA': caaval.to_text()})
    except dns.resolver.NoAnswer:
        final.update({'CAA': 'No Record'})
    print(final)
    name = str(args.value).replace('.','') + '.txt'
    with open(name,'w') as file:
        file.write(str(final))
        file.close()
except Exception as e:
    sys.stderr.write(str(e))
    exit(-1)
