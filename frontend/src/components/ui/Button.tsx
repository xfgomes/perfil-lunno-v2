import { ButtonHTMLAttributes } from "react";
import cn from "classnames";
export default function Button(props: ButtonHTMLAttributes<HTMLButtonElement>){
  const { className, ...rest } = props;
  return <button className={cn("app-btn", className)} {...rest} />
}
