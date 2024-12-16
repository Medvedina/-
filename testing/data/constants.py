import errors.errors as er
import ipaddress
errors = [er.DivZero, er.BracketError, er.InputError, er.BanListError,
          er.BanListRangeError, er.InvalidNumberError, er.PrefixError,
          ipaddress.AddressValueError, ipaddress.NetmaskValueError]