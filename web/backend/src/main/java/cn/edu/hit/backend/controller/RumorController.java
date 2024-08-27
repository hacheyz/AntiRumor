package cn.edu.hit.backend.controller;

import cn.edu.hit.backend.pojo.PageBean;
import cn.edu.hit.backend.pojo.Result;
import cn.edu.hit.backend.pojo.Rumor;
import cn.edu.hit.backend.service.RumorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequestMapping("/rumor")
public class RumorController {
  @Autowired
  private RumorService rumorService;

  //分页查询
  @PostMapping("/pagelist")
  public Result<PageBean<Rumor>> list(@RequestBody Map<String,Object> map){
    return Result.success(rumorService.pagelist(map));
  }
}
