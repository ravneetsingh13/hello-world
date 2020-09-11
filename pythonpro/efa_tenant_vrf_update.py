def efa_tenant_vrf_update(self, dut, **kwargs):
        """
        Syntax::
            dut.efa_tenant_vrf_update(*args,**kwargs)

        * dut – Dut object.
        * *args – Variable length argument list.
        * **kwargs – Variable length argument list.
        :param args:
                * var_1 (str, ``Optional``)              : description
        :type args: list, optional

        :param kwargs:
                * kwargs_1 (str,``Optional``)                          : description .
                * kwargs_2 (int,``Optional``)                          : description .
        :type kwargs: dict, optional


        Returns:
            * tuple - (return_code, output_str, err_str)
            * return_code 0  - On success
            * return_code -1 - On error

        Authors:
            user_name@extremenetworks.com

        Notes:
            Modifications(user-date-reason):

        **PreviousDocument**::

            Purpose :  Update VRFSyntax  :  efa_tenant_vrf_update(vrf_name=\'vrf1\',tenant_name=\'tenant1\',rt_type=\'both\',rt=\'10:10\',ipv4_static_route_next_hop=\'10.101.2.0/24,10.101.1.2\',       ipv6_static_route_next_hop=\'3001:101::/64,2001:101::2\',local_asn=65661,ipv4_static_route_bfd=\'2001:101::2,2001:101::1,300,3,3\',       ipv6_static_route_bfd=\'3001:101::2,3001:101::1,600,600,6\',operation=\'static-route-add\')Syntax  :  efa_tenant_vrf_update(vrf_name=\'vrf1\',tenant_name=\'tenant1\',)Args :    vrf_name    --   Mandatory --  Name of the VRF -- str    tenant_name --   Mandatory --  Name of the tenant  -- str    local_asn -- Optional -- IPv6 Static route network and nexthop seperated by ,. Example 2001:1::/64,3001::2 -- str    ipv4_static_route_bfd -- Optional -- IPv4 Static Route BFD in the format dest-ipv4-addr,source-ipv4-addr[,interval,min-rx,multiplier] Ex 1.1.1.1,2.2.2.2,123,456,3 -- list    ipv6_static_route_bfd -- Optional -- IPv6 Static Route BFD in the format dest-ipv6-addr,source-ipv6-addr[,interval,min-rx,multiplier] Example 1::1,2::2,300,300,3 -- list    ipv4_static_route_next_hop -- Optional -- IPv4 Static route network and nexthop seperated by ,. Example 20.0.0.0/24,16.0.0.2 -- list    ipv6_static_route_next_hop -- Optional -- IPv6 Static route network and nexthop seperated by ,. Example 2001:1::/64,3001::2 -- list    operation -- Optional -- Valid value is local-asn-add | local-asn-delete | static-route-bfd-add | static-route-bfd-delete | static-route-add | static-route-delete -- strReturns :    tuple   --  (return_code, output_str, err_str, parsed_dict).    return_code 0  -- On success ( err_str = null && output_str = result).                -1  -- On error (err_str = captured error && output_str = null).Author :       rnori@extremenetworks.comModifications(user-date-reason) :
    """
        module_name = kwargs["MODULE"]
        tc_dut_log = get_tc_dut_logger(module_name, dut.name)
        access_token = json.load(open((get_out_dir() + "/access_token.txt")))
        headers = {
            "Content-Type": "application/json",
            "Authorization": "{} {}".format(
                access_token["type"], access_token["token"]
            ),
        }

        kwargs_var = {"headers": headers}

        payload = {}

        if ("tenant_name" not in list(kwargs.keys())) and (
            "vrf_name" not in list(kwargs.keys())
        ):
            err = "Mandatory argument tenant_name and vrf_name is missing"
            tc_dut_log.error(err)
            return ((-1), "", err)
        else:
            payload["tenantName"] = kwargs["tenant_name"]
            payload["name"] = kwargs["vrf_name"]

        if "local_asn" in list(kwargs.keys()):
            payload["localAsn"] = kwargs["local_asn"]

        if "operation" in list(kwargs.keys()):
            payload["operation"] = kwargs["operation"]

        static-route-bfd = []
        static-route = []
        if "ipv4_static_route_bfd" in list(kwargs.keys()):
            for ipv4_static_route_bfd in kwargs["ipv4_static_route_bfd"]:
                cmd += ((" " + "--ipv4-static-route-bfd") + " ") + ipv4_static_route_bfd
        if "ipv6_static_route_bfd" in list(kwargs.keys()):
            for ipv6_static_route_bfd in kwargs["ipv6_static_route_bfd"]:
                cmd += ((" " + "--ipv6-static-route-bfd") + " ") + ipv6_static_route_bfd
        if "ipv4_static_route_next_hop" in list(kwargs.keys()):
            for ipv4_static_route in kwargs["ipv4_static_route_next_hop"]:
                cmd += (
                    (" " + "--ipv4-static-route-next-hop") + " "
                ) + ipv4_static_route
        if "ipv6_static_route_next_hop" in list(kwargs.keys()):
            for ipv6_static_route in kwargs["ipv6_static_route_next_hop"]:
                cmd += (
                    (" " + "--ipv6-static-route-next-hop") + " "
                ) + ipv6_static_route

        api_ctx = dut.dca_tenant_vrf_update(vrf_name, tenant_name, cmd)
        (ret, out, err) = api_ctx.get_result()
        if ret == (-1):
            tc_dut_log.error(("Unable to execute cli : %s " % err))
        return (ret, out, err)
